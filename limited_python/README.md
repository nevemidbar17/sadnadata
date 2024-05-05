## limited resources python docker image

This docker image can be used to run python with limited resources.
Limitations are specified in `limit_resources.py`.

### Build:

```
docker build . -t "limited_python"
```

### Run:
```
docker run -b .:/src limited_python /src my_main
```

You should use the `docker compose`
