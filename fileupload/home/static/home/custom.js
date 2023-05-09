// csrf token
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

// csrf token





FilePond.registerPlugin(
    FilePondPluginImagePreview,

);

const pond = FilePond.create(document.querySelector('.my-pond'));

var url = null

function upload_file() {
    var files = pond.getFiles()
console.log("files are ",files)


    var formdata = new FormData()

    console.log("formdata", formdata)
    

    for (var i = 0; i < files.length; i++) {
        formdata.append('files', files[i].file)
    }

    var url = "http://127.0.0.1:8000/handle/"
    
    fetch(url, 
        {
            method: 'POST',
            headers: {'Content-Type': 'multipart/form-data',
                'X-CSRFToken': csrftoken, 
        },
            body: formdata,

        }).then(res => {
            console.log(res.status)
            console.log(res.ok)

            res.json()

        }).then(result => {
            console.log(result)

            // url = `http://127.0.0.1:8000/download/${result.data.folder}`

            // document.getElementById('btn').style.display = ''df -h
            

        })

}

function copyClip() {
    console.log('dd')

 
    /* Copy the text inside the text field */
    navigator.clipboard.writeText(url);

    /* Alert the copied text */
    alert("Copied the text: " + url);
}