function moveTask(objx, NewStatus) {
//    var token = document.getElementsByName("csrfToken").value;
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function(){
        if (this.readyState == 4 && this.status == 200){
            if (NewStatus==1){
            document.getElementById("in_doing_col").appendChild(objx.parentNode)
            }
            if(NewStatus==2){
                document.getElementById("done_col").appendChild(objx.parentNode)
            }
            if(NewStatus==3|| NewStatus==0){
                objx.parentNode.parentNode.removeChild(objx.parentNode)
            }
            setButton(NewStatus, objx)
        }
    }
    xhttp.open("GET","/task/edit");
//    xhttp.setRequestHeader('csfrtoken',token);
    xhttp.setRequestHeader("ID", objx.parentNode.querySelector(".invisible").innerHTML);
    xhttp.setRequestHeader("NewStatus", NewStatus);
    xhttp.send();
}

function setButton(Status, obj){
    if (Status==1){
        obj.parentNode.classList.remove("bg-warning")
        obj.parentNode.classList.add("bg-primary")
        obj.textContent = "It's done"
        obj.classList.add('btn-success')
        obj.classList.remove('btn-info')
        obj.onclick = function() {moveTask(this,2)}
    }
    if (Status==2){
        obj.parentNode.classList.add("bg-success")
        obj.parentNode.classList.remove("bg-primary")
        obj.textContent = "Archive it"
        obj.classList.remove('btn-success')
        obj.classList.add('btn-danger')
        obj.onclick = function() {moveTask(this,3)}
    }


}
