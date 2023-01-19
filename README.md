# Partnership matcher

This project aims to make group projects easier by automatically finding you partners for small teams. It is able to select partners not based on your mentioned preferences, but in an impatial way exposing several endpoints in a user-facing API which later connects to the business logic API where the magic happens. The user-facing endpoints are as follows:


#### API ENDPOINTS
```http
  POST /give_me_partener/
```

| Body | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `user_id`     | `int` | **Required** id of the user that wants a partner|


## APP Overview 

![](app-overview.png)


## Technologies
- [K8S](https://kubernetes.io/)
- [Docker](https://docs.docker.com/)
- [Terraform](https://registry.terraform.io/)
- [Flask](https://flask.palletsprojects.com/en/2.0.x/)
- [MySQL](https://www.mysql.com/)
- [KIND -testing](https://kind.sigs.k8s.io/)
- [MINIKUBE -testing](https://minikube.sigs.k8s.io/docs/start/)
- [POSTMAN -testing](https://www.postman.com/)
- [Pyton 3.8.10](https://www.python.org/downloads/release/python-3810/)



## Usage & Installation

```bash

```

## Contributions

- [Iulia Anghel](https://github.com/iuliiaioana)
- [Lavinia Nedelea](https://github.com/laviniamnedelea)
- [Lorena Comanescu](https://github.com/Lorena71999)
