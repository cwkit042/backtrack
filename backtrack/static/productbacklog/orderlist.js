

document.addEventListener('DOMContentLoaded', function(){
  cumulativeStoryPoint = document.getElementsByClassName('cumulativeStoryPoint');
  storyPoint = document.getElementsByClassName('storyPoint');
  var i;
  var cumulativeCounter = 0;
  for (i=0; i<storyPoint.length; i++){
    cumulativeCounter += parseInt(storyPoint[i].innerHTML);
    cumulativeStoryPoint[i].innerHTML = cumulativeCounter;
  }
  document.getElementById('totalStoryPoint').innerHTML = cumulativeCounter;
});

function namePopupFunc(event){
    var val = event.target.getAttribute('value');
    var pbi = document.getElementById(val);
    console.log(val);
    console.log(pbi);
    
    var name = pbi.getElementsByClassName('namePopup')[0].innerHTML;
    console.log(name);
    document.getElementById('titleInModal').innerHTML = "Modify "+name;
    document.getElementById('nameInModal').setAttribute('value', name);
    document.getElementById('storyPointInModal').setAttribute('value', pbi.getElementsByClassName('storyPoint')[0].innerHTML);
    document.getElementById('descriptionInModal').innerHTML = pbi.getElementsByClassName('description')[0].innerHTML;
    document.getElementById('idInModal').setAttribute('value', val);
    document.getElementById('deleteBtn').setAttribute('action', '/productbacklog/deletepbi/');
    document.getElementById('modifyBtn').setAttribute('action', '/productbacklog/modifypbi/');
}

function pbi_delete(){
    event.preventDefault()
    document.getElementById('modifyPBI').setAttribute('action', '/productbacklog/deletepbi/');
    document.getElementById('submit').click();
}

function pbi_modify(){
    event.preventDefault()
    document.getElementById('modifyPBI').setAttribute('action', '/productbacklog/modifypbi/');
    document.getElementById('submit').click();
}