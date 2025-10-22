# procesar_iconos_seguro.py
from rembg import remove, new_session
from PIL import Image
import os, sys, csv, time, hashlib, shutil, tempfile
from pathlib import Path

IN_DIR = Path("C:/Users/Asus/Pictures/objetos")
# -*- coding: utf-8 -*-
# Quita blanco y un poco de gris claro con control fino.
# Guarda en ./only_white_gray_removed
from pathlib import Path
from PIL import Image
import numpy as np
import cv2, tempfile


OUT_DIR = Path("only_white_gray_removed")
OUT_DIR.mkdir(parents=True, exist_ok=True)

# ----- Parámetros de “quitar sin exagerar” -----
RGB_TOL   = 18   # 0..255  píxeles con R,G,B >= 255-RGB_TOL se consideran casi blancos
DELTAE_T  = 10.0 # 0..100  distancia CIEDE2000 máxima a blanco puro (menor = más conservador)
FEATHER   = 2    # px suavizado de borde para evitar halos. 0 desactiva
KEEP_ALPHA = True # respeta alpha original en no-blancos

def atomic_save_pil(img: Image.Image, dst: Path):
    with tempfile.NamedTemporaryFile(delete=False, dir=str(dst.parent), suffix=dst.suffix) as tmp:
        tmp_path = Path(tmp.name)
    try:
        img.save(tmp_path)
        tmp_path.replace(dst)
    except Exception:
        try: tmp_path.unlink(missing_ok=True)
        except Exception: pass
        raise

def rgb_to_lab(img_rgb_u8):
    return cv2.cvtColor(img_rgb_u8, cv2.COLOR_RGB2LAB)

def ciede2000_lab(lab1, lab2):
    # lab1, lab2: arrays float32 de shape (...,3)
    # Implementación vectorizada aproximada pero estable (basada en Sharma 2005)
    L1, a1, b1 = lab1[...,0], lab1[...,1], lab1[...,2]
    L2, a2, b2 = lab2[...,0], lab2[...,1], lab2[...,2]

    C1 = np.hypot(a1, b1)
    C2 = np.hypot(a2, b2)
    Cm = (C1 + C2) / 2.0
    G = 0.5 * (1 - np.sqrt((Cm**7) / (Cm**7 + 25**7)))
    a1p = (1 + G) * a1
    a2p = (1 + G) * a2
    C1p = np.hypot(a1p, b1)
    C2p = np.hypot(a2p, b2)

    hp_f = lambda a, b: np.degrees(np.arctan2(b, a)) % 360.0
    h1p = hp_f(a1p, b1)
    h2p = hp_f(a2p, b2)

    dLp = L2 - L1
    dCp = C2p - C1p

    dhp = h2p - h1p
    dhp = np.where(dhp > 180, dhp - 360, dhp)
    dhp = np.where(dhp < -180, dhp + 360, dhp)
    dHp = 2 * np.sqrt(C1p * C2p) * np.sin(np.radians(dhp / 2.0))

    Lpm = (L1 + L2) / 2.0
    Cpm = (C1p + C2p) / 2.0

    hps = np.where(np.abs(h1p - h2p) > 180, (h1p + h2p + 360) / 2.0, (h1p + h2p) / 2.0)
    hpm = np.where((C1p*C2p) == 0, h1p + h2p, hps)

    T = (1
         - 0.17 * np.cos(np.radians(hpm - 30))
         + 0.24 * np.cos(np.radians(2 * hpm))
         + 0.32 * np.cos(np.radians(3 * hpm + 6))
         - 0.20 * np.cos(np.radians(4 * hpm - 63)))

    Sl = 1 + (0.015 * (Lpm - 50)**2) / np.sqrt(20 + (Lpm - 50)**2)
    Sc = 1 + 0.045 * Cpm
    Sh = 1 + 0.015 * Cpm * T

    Rt = -2 * np.sqrt((Cpm**7) / (Cpm**7 + 25**7)) * \
         np.sin(np.radians(60 * np.exp(-((hpm - 275) / 25)**2)))

    dE = np.sqrt(
        (dLp / Sl)**2 +
        (dCp / Sc)**2 +
        (dHp / Sh)**2 +
        Rt * (dCp / Sc) * (dHp / Sh)
    )
    return dE

for src in sorted(IN_DIR.glob("*.png")):
    if OUT_DIR in src.parents:
        continue
    im = Image.open(src).convert("RGBA")
    arr = np.array(im)
    rgb = arr[...,:3].copy()
    alpha = arr[...,3].copy()

    # Máscara por RGB puro cerca de blanco
    near_white_rgb = (rgb[...,0] >= 255 - RGB_TOL) & \
                     (rgb[...,1] >= 255 - RGB_TOL) & \
                     (rgb[...,2] >= 255 - RGB_TOL)

    # Máscara por “parecido a blanco” en espacio perceptual (CIEDE2000)
    lab   = rgb_to_lab(rgb.astype(np.uint8)).astype(np.float32)
    white_lab = np.array([100.0, 0.0, 0.0], dtype=np.float32)  # blanco puro en Lab aprox
    white_like = ciede2000_lab(lab, white_lab).astype(np.float32) <= DELTAE_T

    # Unión conservadora: quita si es casi blanco por RGB O similar por Lab
    mask_remove = near_white_rgb | white_like

    # Feather opcional para evitar dientes en el borde de lo quitado
    if FEATHER > 0:
        k = FEATHER*2 + 1
        blur = cv2.GaussianBlur(mask_remove.astype(np.uint8)*255, (k, k), 0)
        # reescala a probabilidad 0..1
        prob = (blur.astype(np.float32) / 255.0).clip(0,1)
        new_alpha = (alpha.astype(np.float32) * (1.0 - prob)).astype(np.uint8)
    else:
        new_alpha = np.where(mask_remove, 0, alpha)

    if KEEP_ALPHA:
        # mantiene alpha original donde no se quita
        pass

    out = arr.copy()
    out[...,3] = new_alpha
    out_img = Image.fromarray(out, "RGBA")
    atomic_save_pil(out_img, OUT_DIR / f"{src.stem}.png")

    removed = int(mask_remove.sum())
    print(f"OK -> {src.stem}.png  | removidos≈{removed} px")
