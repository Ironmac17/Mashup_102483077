const form = document.getElementById("mashupForm");
const toast = document.getElementById("toast");

function showToast(msg){
    toast.innerText = msg;
    toast.classList.add("show");
}

function hideToast(){
    setTimeout(()=>toast.classList.remove("show"),4000);
}

form.addEventListener("submit", async function(e){
    e.preventDefault();

    const formData = new FormData(form);

    try{
        showToast("Downloading videos...");
        await new Promise(r=>setTimeout(r,1000));

        showToast("Converting audio...");
        await new Promise(r=>setTimeout(r,1000));

        showToast("Creating mashup...");

        const response = await fetch("/",{
            method:"POST",
            body:formData
        });

        await response.text();

        showToast("Mashup ready. Email sent successfully!");
        hideToast();

    }catch(err){
        showToast("Error occurred");
    }
});
