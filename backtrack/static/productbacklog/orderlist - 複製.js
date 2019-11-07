

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
