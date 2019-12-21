# Show & Tell API

[![License](http://img.shields.io/badge/License-MIT-brightgreen.svg)](./LICENSE)

Neural Image Caption Generator - Show and Tell for project [EyeSpace](https://eyespace.app/). Project was inspired by [Show and Tell: A Neural Image Caption Generator](https://arxiv.org/pdf/1411.4555.pdf).

## Getting Started

<!-- These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system. -->

### Dependencies 

* python 3.6.8
* keras 2.2.4 
* numpy 1.15.4
* nltk 3.4
* Pillow
* tensorflow
* matplotlib
* Flask
* PM2

### Installing
To start the development server:

```
python3 app.py
```

To start the production server:

```
sudo pm2 start app.py --name show-tell-api --interpreter=python3
```
### Testing

To test from a local machine:
```
curl -X POST -d @request.json http://ip.ad.dre.ss/test --header "Content-Type:application/json"
```
## Built With

* [Flask](http://flask.palletsprojects.com/en/1.1.x/) - Python Server for the API
* [Keras](https://keras.io/) - API on Tensorflow for the Model
* [PM2](https://pm2.keymetrics.io/) - For Loadbalancing and Deployment
<!-- 
## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags).  -->

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
<!-- 
## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc -->

