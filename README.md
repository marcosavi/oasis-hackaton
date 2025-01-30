# ED#14 Oasis - Oaizs.com & OasisConnect

<font size="4px">Oasis provides training and resources to current and future teachers in underserved regions for quality education. The Web-App, www.oaizs.com, is primarily developed using Django, a Python framework. Additionally, for accepting future donations, we used Stripe.

However, in addition to software, our team developed OasisConnect. It creates a reliable network for schools, enabling access to oaizs.com without the need for teachers to have access to the internet. It can be easily installed in any location where people gather to learn, enabling both teachers to access resources to ease their teachings or be a place where future teachers gather to access the online trainings that we offer.

OasisConnect is built using a Raspberry Pi 5 16GB. More details on the branch [oasisconnect](https//github.com/marcosavi/oasis-hackaton/tree/oasisconnect).
</font>

## Installation

1. Clone the repository

```bash
git clone
```

2. Install the dependencies

```bash
pip install -r requirements.txt
```

3. Run the server

```bash
python manage.py migrate
python manage.py runserver
```
