"""
inv up
    Запускает компоуз в продуктовом режиме
inv up -d front 
    Запускает разработку фронта, а весь остальной компоуз в продуктовом режиме
inv up -d api
    Запускает разработку апи, а весь остальной компоуз в продуктовом режиме

Запуски в разработке можно комбинировать таким образом: 
inv up -d front -d api
... (просто перед каждым тегом ставить флаг -d)


Нельзя добавить новый контейнер для разработки путем написания ещё одной команды inv up -d [с соответствующим тегом]
Придется каждый раз перечислять полный список контейнеров, которые должны быть запущены в режиме разработки 
(это происходит потому, что os.environ[...] = ... устанавливает переменную среды только на время 
исполнения процесса python (или его дочерних процессов))


Каждый новый inv up перезапускает только те контейнеры, которые сменили режим
Остальные остаются нетронутыми

inv down
    Вырубает компоуз
"""

import os
from invoke import task

os.environ["API_MODE"] = getattr(os.environ, "API_MODE", "prod")
os.environ["FRONT_MODE"] = getattr(os.environ, "FRONT_MODE", "prod")

@task(iterable=["d"])
def up(ctx, d):
    if "front" in d:
        os.environ["FRONT_MODE"] = "dev"
    if "api" in d:
        os.environ["API_MODE"] = "dev"
    ctx.run(f'docker-compose -f "docker-compose.yaml" up -d --build')
    ctx.run("echo -en '\033[0;31mapi: \033[0;32m'${API_MODE} '\033[0;31mfront: \033[0;32m'${FRONT_MODE}'\n'")


@task
def down(ctx):
    ctx.run(f'docker-compose -f "docker-compose.yaml" down')
