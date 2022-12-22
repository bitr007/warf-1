
echo "BUILD START"
docker build -t warf .
docker run --name warf -d -p 8000:8000 warf
echo "BUILD END"
