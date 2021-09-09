# https://github.com/tamccullough - questions? twitter @tamccullough
from flask import Flask, jsonify, request, send_file

# for this file to not be so long, I have placed a dictionary in the following py file
# to edit there. Saves some clutter in this area
import utils as utils

# edit this file however you see fit. If it suits you to make changes to it for your work. Do so.

# set the name for the collection
collection_name = "Plant Shop"

app = Flask(__name__)

# serve the json file metadata required for the token
@app.route("/<plant_dna>")  # url includes the token_id number
def item(plant_dna):
    plant_dna = int(plant_dna)
    if plant_dna < 1 or utils.check_length(plant_dna) != 16:
        return jsonify({"error": "improper format"}), 400
    dna_chunks = utils.split_dna(plant_dna)
    genus = dna_chunks[0]
    species = dna_chunks[1]
    color = dna_chunks[2]
    variant = dna_chunks[3]
    # data for the collection of images is stored in a csv file, loaded into a dataframe
    # get the relevant slice from the dataframe, selecting from the token_id
    # get the url root which will be printed for the nft reference
    url_path = request.url_root
    # external_url = 'https://testnets.opensea.io/assets/<asset_contract_address>/{token_id}'

    # taking the
    attributes = []
    attributes.append(utils.create_attribute("genus", genus))
    attributes.append(utils.create_attribute("species", species))
    attributes.append(utils.create_attribute("color", color))
    attributes.append(utils.create_attribute("variant", variant))

    # using Flask jsonify to pass the selected data as json file format
    return jsonify(
        {
            "name": f"{collection_name} #{plant_dna+1}",
            "external_url": f"{url_path}{plant_dna}",
            "image": f"{url_path}image/{plant_dna}",
            "description": f"{collection_name} game",
            "attributes": attributes,
        }
    )


# serve the selected image, important for the image to show up within the nft
@app.route("/image/<token_id>")
def image(token_id):
    token_id = int(token_id)
    # if you haven't named your images using a lower case version of your collection name
    # you need to change the following string to point to the images
    image_url = f"collection/{collection_name.lower()}{token_id+1}.png"

    return send_file(image_url, mimetype="image/png")


if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
