# Gym API

This is a server that provides basic API for Gym Application

## Installation

Use Docker and Docker Compose to build and run a server
```bash
docker-compose build
docker-compose up
```

## API Description
It contains several parts to interact with

* Gym (/gyms/) - basically gym (connected with Location and Network)
* Location (/gyms/locations/) - gyms location
* Network (/gyms/networks/) - gyms network (like, under one business)
* SubscriptionPlan (/subscriptions/plans/) - subscription plans available at gyms
* SubscriptionFeature (/subscriptions/features/) - features to be included in plans to buy and use
* Attendance (/subscriptions/callback/attend/) - feature to be called when a man or woman came to gym and used a passkey (automatically track attendance and check do customer have rights to attend a gym)
* Token (/token/) - provide JWT Token authorization (based on it we can restrict accesses)
* User (/users/) - provide CRUD (C as feature to register) and ability to change password for user
* UserAccessability - connection between user and features from plan that he bought

## Run Tests

If you want to run tests, run inside 'web' container
```python
pytest
```