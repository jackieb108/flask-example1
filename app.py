import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
#openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_type = "azure"
openai.api_base = "https://cto-oai.openai.azure.com/"
openai.api_version = "2022-12-01"
openai.api_key = ""

@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        animal = request.form["animal"]
        response = openai.Completion.create(
            #model="text-davinci-003",
            #prompt=generate_prompt(animal),
            #temperature=0.6,
            engine="CTODaVinci",
            #prompt="Below is an extract from the annual financial report of a company. Extract key financial number (if present), key internal risk factors, and key external risk factors.\n\n# Start of Report\nRevenue increased $7.5 billion or 16%. Commercial products and cloud services revenue increased $4.0 billion or 13%. O365 Commercial revenue grew 22% driven by seat growth of 17% and higher revenue per user. Office Consumer products and cloud services revenue increased $474 million or 10% driven by Consumer subscription revenue, on a strong prior year comparable that benefited from transactional strength in Japan. Gross margin increased $6.5 billion or 18% driven by the change in estimated useful lives of our server and network equipment. \nOur competitors range in size from diversified global companies with significant research and development resources to small, specialized firms whose narrower product lines may let them be more effective in deploying technical, marketing, and financial resources. Barriers to entry in many of our businesses are low and many of the areas in which we compete evolve rapidly with changing and disruptive technologies, shifting user needs, and frequent introductions of new products and services. Our ability to remain competitive depends on our success in making innovative products, devices, and services that appeal to businesses and consumers.\n# End of Report\n\n# Solution\n\n## Key Financial Numbers\n\n1. Revenue increased $7.5 billion or 16%.\n2. Gross margin increased $6.5 billion or 18%\n\n## Key Internal Risk Factors\n\n1. Our competitors range in size from diversified global companies with significant research and development resources to small, specialized firms whose narrower product lines may let them be more effective in deploying technical, marketing, and financial resources.\n2. Barriers to entry in many of our businesses are low and many of the areas in which we compete evolve rapidly with changing and disruptive technologies, shifting user needs, and frequent introductions of new products and services.\n3. Our ability to remain competitive depends on our success in making innovative products, devices, and services that appeal to businesses and consumers.\n\n## Key External Risk Factors\n\n1. Our competitors range in size from diversified global companies with significant research and development resources to small, specialized firms whose narrower product lines may let them be more effective in deploying technical, marketing, and financial resources.\n2. Barriers to entry in many of our businesses are low and many of the areas in which we compete evolve rapidly with changing and disruptive technologies, shifting user needs, and frequent introductions of new products and services.\n3. Our ability to remain competitive depends on our success in making innovative products, devices, and services that appeal to businesses and consumers.\n\n## Key Financial Numbers\n\n1. Revenue increased $7.5 billion or 16%.\n2. Gross margin increased $6.5 billion or 18%\n\n## Key Internal Risk Factors\n\n1. Our competitors range in size from diversified global companies with significant research and development resources",
            #prompt=generate_prompt(animal),
            prompt=animal,
            #prompt="Write a product launch email for new AI-powered headphones that are priced at $79.99 and available at Best Buy, Target and Amazon.com. The target audience is tech-savvy music lovers and the tone is friendly and exciting.\n\n1. What should be the subject line of the email?  \n2. What should be the body of the email?",
            temperature=0.3,
            max_tokens=350,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            best_of=1,
            stop=None
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(animal):
    return """Suggest three names for an animal that is a superhero.

Animal: Cat
Names: Captain Sharpclaw, Agent Fluffball, The Incredible Feline
Animal: Dog
Names: Ruff the Protector, Wonder Canine, Sir Barks-a-Lot
Animal: {}
Names:""".format(
        animal.capitalize()
    )

def generate_prompt_icf(animal):
    return """Suggest three names for an animal that is a superhero.

Animal: Cat
Names: Captain Sharpclaw, Agent Fluffball, The Incredible Feline
Animal: Dog
Names: Ruff the Protector, Wonder Canine, Sir Barks-a-Lot
Animal: {}
Names:""".format(
        animal.capitalize()
    )