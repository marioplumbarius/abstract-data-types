#### Download vagrant
[http://www.vagrantup.com/downloads](http://www.vagrantup.com/downloads)

#### Install vagrant hostname plugin
So you can access the app from your browser at: app.cademinhabreja instead of a IP address.
```shell
$ vagrant plugin install vagrant-hostsupdater
```

#### Download vagrant precise32 box
The development environment runs on a lightweight linux instance.
```shell
$ vagrant box add hashicorp/precise32
```

#### Start the vm
Head over to the vagrant directory from the repository source code and start the vm.
```shell
$ cd cade-minha-breja/vagrant/ && vagrant up
```

#### Provisioning the vm
This ensures the provision with puppet.
```shell
$ vagrant provision
```

#### Log into the vm
```shell
$ vagrant ssh
```

#### Head over to the app root directory
```shell
$ cd /opt/cade-minha-breja
```

#### Start the web server sample
```shell
$ python sample.py
```
**You should see the following output:**
```shell
$ Running on http://0.0.0.0:5000/
```

There are some registered routes for the sample app, you might play with some of them:
- GET /
- GET /users
- GET /users/:user_id
- GET /beers
- GET /log