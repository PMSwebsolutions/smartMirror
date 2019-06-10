function clock(){
  var now = new Date();
  var time = now.toLocaleTimeString();
  var weekday = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
  var months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];


  var date = weekday[now.getDay()] + ", " + now.getDate() + " " + months[now.getMonth()];
  var timeLen = time.length;
  if(timeLen == 10){
    document.querySelector(".time").innerHTML = time.substr(0,4);
  }else {
    document.querySelector(".time").innerHTML = time.substr(0,5);
  }
  document.querySelector(".date").innerHTML = date;
  setTimeout(clock, 1000);
}

clock();
