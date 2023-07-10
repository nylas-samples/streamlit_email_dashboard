# streamlit_email_dashboard

This sample will show you how to create an email dashboard using Streamlit.

You can follow along step-by-step in our blog post ["Streamlit: Building an Email Dashboard"](https://www.nylas.com/blog/streamlit-building-an-email-dashboard/).

## Setup

### System dependencies

- Python v3.x

### Gather environment variables

You'll need the following values:

```text
CLIENT_ID = ""
CLIENT_SECRET = ""
ACCESS_TOKEN = ""
```

Add the above values to a new `.env` file:

```bash
$ touch .env # Then add your env variables
```

### Install dependencies

```bash
$ pip3 install streamlit # Pure Python package that allows you to create data scripts into web apps in minutes
$ pip3 install python-dotenv # Environment variables
$ pip3 install matplotlib # Library for creating static, animated, and interactive visualizations
$ pip3 install pandas # Python data analysis library
```

## Usage

Run the file **streamlit_email_dashboard.py**:

```bash
$ streamlit run streamlit_email_dashboard.py
```

Streamlit will open up your browser on port 8510.

## Learn more

Visit our [Nylas Python SDK documentation](https://developer.nylas.com/docs/developer-tools/sdk/python-sdk/) to learn more.
