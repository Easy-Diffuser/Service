sendToEasyDiffuser = async function (context) {
    var imageUrl = context.srcUrl

    const Url = 'http://127.0.0.1:9889';

    const response = await fetch(Url, {
        headers: {
            'content-type': 'text/plain',
        },
        body: imageUrl,
        method: 'POST',
    });

    return response.json();
};

chrome.contextMenus.create({
    title: "Easy Diffuser로 불러오기",
    contexts: ["image"],  // ContextType
    onclick: sendToEasyDiffuser // A callback function
});