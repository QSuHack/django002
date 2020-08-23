let progress_population = document.getElementById("progress_bar_population");
let progress_members = document.getElementById("progress_bar_country");

function update_bar(){
    progress_val_population = 0;
    checkboxes = document.getElementsByClassName("checkbox");
    progress_members_num = 0;
    for (ch in checkboxes)
    {
        if (checkboxes[ch].checked == true){
            progress_val_population += DATA_JS.find((el)=>el[0] === checkboxes[ch].getAttribute("name"))[1]/population_total*100;
            progress_members_num +=1;
        }
    }
    progress_population.style.width =progress_val_population+"%" ;
    progress_population.setAttribute("aria-valuenow", progress_val_population) ;
    progress_population.textContent = "Population: "+Math.round(progress_val_population*100)/100+"%" ;
    progress_members.style.width = progress_members_num/number_of_members*100+"%";
    progress_members.setAttribute("aria-valuenow", progress_members_num);
    progress_members.textContent = "Country: "+Math.round(progress_members_num  /number_of_members*10000)/100+"%";
    progress_members.classList.remove("bg-success")
    progress_population.classList.remove("bg-success")
    progress_members.classList.remove("bg-danger")
    progress_population.classList.remove("bg-danger")
    if (progress_members_num>=4){
        progress_members.classList.add("bg-danger")
    }
    if (progress_val_population>=35){
        progress_population.classList.add('bg-danger')
    }
    
    if( progress_members_num >= Math.round(number_of_members*0.55)){
        progress_members.classList.remove("bg-danger")
        progress_members.classList.add("bg-success")
    }
    if(progress_val_population>=65){
        progress_population.classList.remove("bg-danger")
        progress_population.classList.add("bg-success")
    }
}
