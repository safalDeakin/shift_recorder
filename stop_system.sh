docker compose -f ci_cd/docker-compose.yml down &&
docker compose -f data_server/docker-compose.yml down &&
docker compose -f shift_recorder/docker-compose.yml down;