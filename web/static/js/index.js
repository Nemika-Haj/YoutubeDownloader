const downloadVideoButton = document.getElementById("downloadVideo")
const downloadVideoUrl = document.getElementById("youtubeVideoURL")

const loader = document.getElementById("loader")

function toggleLoad() {
    loader.checked = !loader.checked
}

let done = {
    div: document.getElementById("downloadDone"),
    header: document.getElementById("doneHeader"),
    text: document.getElementById("doneDescription")
}

function downloadBox(success) {

    console.log(success)

    if (success) {
        done.header.innerText = "Download Successful"
        done.text.innerText = "Your video was downloaded! Check your desktop for a folder named 'Youtube Downloader'!"

        done.div.style.backgroundColor = "#32b209"
        done.div.style.display = "block"
        done.div.style.right = "10px"

    } else {
        done.header.innerText = "Download Failed"
        done.text.innerText = "There was an unexpected error downloading your video. Try checking if the URL is valid."

        done.div.style.backgroundColor = "#fe070b"
        done.div.style.display = "block"
        done.div.style.right = "10px"

    }

    setTimeout(() => {
        done.div.style.right = "-1000px"
        done.div.style.display = "none"
    }, 5000)

}

downloadVideoButton.addEventListener("click", () => {
    toggleLoad()

    let type = "video"

    eel.download(downloadSongUrl.innerText, type)((result) => {
        toggleLoad()
        downloadBox(result)
    })

})

const downloadSongButton = document.getElementById("downloadSong")
const downloadSongUrl = document.getElementById("youtubeSongURL")

downloadSongButton.addEventListener("click", () => {
    toggleLoad()

    let type = "song"

    eel.download(downloadSongUrl.innerText, type)((result) => {
        console.log(result)
        toggleLoad()
        downloadBox(result)
    })

})

window.oncontextmenu = function(event) {
    // block right-click / context-menu
    event.preventDefault();
    event.stopPropagation();
    return false;
};