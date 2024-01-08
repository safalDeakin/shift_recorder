docker compose -f ci_cd/docker-compose.yml up -d &&
docker compose -f data_server/docker-compose.yml up -d &&
docker compose -f shift_recorder/docker-compose.yml up -d;