const copy = (text) => {
  const $textarea = document.createElement("textarea");

  document.body.appendChild($textarea);

  $textarea.value = text;
  $textarea.select();

  document.execCommand("copy");
  document.body.removeChild($textarea);
};

async function getData(option) {
  const imageUrl = document.getElementById("image").src;

  const Url = "http://127.0.0.1:5998";

  const response = await fetch(Url, {
    headers: {
      "content-type": "text/plain",
    },
    body: option + imageUrl,
    method: "POST",
  });

  return response.json();
}

const extractClickPart = document.getElementById("extract-button");
const extractClick = extractClickPart.firstElementChild;
const loader = extractClickPart.lastElementChild;

extractClick.addEventListener("click", async () => {
  if (document.getElementById("to_tag").checked === true) {
    extractClick.style.display = "none";
    loader.style.display = "block";

    const result = await getData("tag");

    const pos_element = document.getElementById("positive_card");

    pos_element.innerHTML = "";

    for (const tag of result["pos"]) {
      const chip = document.createElement("div");
      chip.setAttribute("class", "chip");

      const i = document.createElement("i");
      i.setAttribute("class", "close material-icons");
      i.innerHTML = "close";

      chip.innerHTML = tag;
      chip.appendChild(i);

      pos_element.appendChild(chip);
    }

    const neg_element = document.getElementById("negative_card");

    neg_element.innerHTML = "";

    for (const tag of result["neg"]) {
      const chip = document.createElement("div");
      chip.setAttribute("class", "chip");

      const i = document.createElement("i");
      i.setAttribute("class", "close material-icons");
      i.innerHTML = "close";

      chip.innerHTML = tag;
      chip.appendChild(i);

      neg_element.appendChild(chip);
    }

    extractClick.style.display = "block";
    loader.style.display = "none";

    extractClick.setAttribute("class", "btn-flat disabled");
  }
  
  if (document.getElementById("to_img").checked === true) {
    extractClick.style.display = "none";
    loader.style.display = "block";

    const result = await getData("img");

    const res_element = document.getElementById("result");
    res_element.innerHTML = "";

    const dd = document.createElement("div");
    dd.setAttribute("class", "container");
    dd.setAttribute("style", "max-width: 350px; align-items: center;");

    const d = document.createElement("div");
    d.setAttribute("class", "row center");

    const i = document.createElement("img");
    i.setAttribute(
      "style",
      "margin-left: auto; margin-right: auto; width: 100%; max-width: 350px;"
    );

    i.setAttribute("src", "./output/output.png");

    d.appendChild(i);
    dd.appendChild(d);
    res_element.appendChild(dd);

    extractClick.style.display = "block";
    loader.style.display = "none";

    extractClick.setAttribute("class", "btn-flat disabled");
  }
});

const positiveClick = document.getElementById("positive-button");

positiveClick.addEventListener("click", async () => {
  const positive_card = document.getElementById("positive_card");

  const positive_elements = positive_card.childNodes;

  let tags = "";

  for (const element of positive_elements) {
    const tag = element.innerText.split("\n")[0];

    tags += " ";
    tags += tag;
  }

  copy(tags);
  alert("Positive Prompt Copied");
});

const negativeClick = document.getElementById("negative-button");

negativeClick.addEventListener("click", async () => {
  const negative_card = document.getElementById("negative_card");

  const negative_elements = negative_card.childNodes;

  let tags = "";

  for (const element of negative_elements) {
    const tag = element.innerText.split("\n")[0];

    tags += " ";
    tags += tag;
  }

  copy(tags);
  alert("Negative Prompt Copied");
});
