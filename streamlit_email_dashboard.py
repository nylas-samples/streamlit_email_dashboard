# Import your dependencies
from nylas import Client
import streamlit as st
from wordcloud import WordCloud
import os
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt
from dotenv import load_dotenv
from nylas.models.messages import ListMessagesQueryParams

# Load your env variables
load_dotenv()

# Initialize your Nylas API client
# Initialize Nylas client
nylas = Client(
    api_key = os.environ.get("V3_API_KEY")
)

# Auxiliar variables
from_messages = []
to_messages = []
text = ""

st.title('Email Dashboard')
num = st.slider('How many emails?', 1, 200, 50)

# Create query parameters
f_query_params = ListMessagesQueryParams(
	{'in' : "inbox",
	'limit': num}
)

# Create query parameters
t_query_params = ListMessagesQueryParams(
	{'in' : "sent",
	'limit': num}
)

# Get emails from your inbox folder
f_messages, _, _ = nylas.messages.list(os.environ.get("GRANT_ID"), f_query_params)
# Get emails from your sent folder
t_messages, _, _ = nylas.messages.list(os.environ.get("GRANT_ID"), t_query_params)
print(f_messages)
# Loop through your inbox emails
for msg in f_messages:
	# Get the name of the person emailing you
	if(msg.from_[0].email != ""):
		from_messages.append(msg.from_[0].email.split()[0])
	# Concatate the subjects of all emails
	text = text + " " + msg.subject
# Turn the array into a data frame	
f_df = pd.DataFrame(from_messages, columns=['Names'])
# Aggregate values, get the top 3 and a name to the new column
top_3_from = f_df["Names"].value_counts().head(3).reset_index(name="count")
top_3_from.columns = ['person', 'count']

# Loop through your sent emails
for msg in t_messages:
	# Get the name of the person you're emailing	
	if(msg.from_[0].email != ""):	
		to_messages.append(msg.to[0].email.split()[0])
# Turn the array into a data frame		
t_df = pd.DataFrame(to_messages, columns=['Names'])
# Aggregate values, get the top 3 and a name to the new column
top_3_to = t_df["Names"].value_counts().head(3).reset_index(name="count")
top_3_to.columns = ['person', 'count']

# Using all the email subjects, generate a wordcloud
wordcloud = WordCloud(width=800, height=300).generate(text)

# Create columns layout
col1, col2 = st.columns(2)
with col1:
	# Create barchart from emails
    bar_chart = alt.Chart(top_3_from).mark_bar().encode(
    alt.X('person', title='person'),
    alt.Y('count', title='count'),
    color='person:N'
    ).properties(
        title='From: Emails'
    )
    # Display the barchart
    st.altair_chart(bar_chart, use_container_width=True)
with col2:
    # Create barchart to emails
    bar_chart = alt.Chart(top_3_to).mark_bar().encode(
    alt.X('person', title='person'),
    alt.Y('count', title='count'),
    color='person:N'
    ).properties(
        title='To: Emails'
    )
    # Display the barchart
    st.altair_chart(bar_chart, use_container_width=True)

# Display the generated image:
fig, ax = plt.subplots(figsize = (12, 8))
ax.imshow(wordcloud)
plt.axis("off")
st.pyplot(fig)
