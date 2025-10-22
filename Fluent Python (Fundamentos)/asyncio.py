"""uso de asyncio para concurrencia inportante la funcion debe ser async para
poder usar await"""
import asyncio
import time
async def slow(x):
    #inportante usar asynciosleep y no sleep
    await asyncio.sleep(1)
    print(f"here {x}")
    return f"THE VALUE IS {x}"

def slow_sin(x):
    #en este caso como no es una async fun entonces si se puede usar sleep
    time.sleep(1)
    print(f"here {x}")
    return f"THE VALUE IS {x}"

async def asyncioo():
    #inicializas el loop
    loop = asyncio.get_running_loop()
    #el gather permite ejecutar varias peticiones asyn al tiempo y las espera hasta el final
    await asyncio.gather(*(slow(x) for x in range(4)))
    #para el caso de funciones no asyn es necesario usar concurrent.futures
    from concurrent.futures import ThreadPoolExecutor
    #hacemos el pool de executer para ejecutar nuestra futeres
    with ThreadPoolExecutor() as executer:
        # dentor de esto si podemos usar with
        await loop.run_in_executor(executer,slow_sin,5)


if __name__ == "__main__":
    asyncio.run(asyncioo())