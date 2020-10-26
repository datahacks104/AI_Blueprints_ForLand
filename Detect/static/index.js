document.addEventListener('DOMContentLoaded', ()=>{
  var dropzone = document.getElementById('dropzone');
  var default_upload = document.getElementsByClassName('upload')[0];
  var click_upload = document.getElementsByClassName('click_upload')[0];
  var gallery = document.getElementsByClassName('gallery')[0];
  var land_button = document.getElementsByClassName('land_button')[0];
  var result = document.getElementsByClassName('result')[0];
  land_button.style.display = 'none';
  console.log('done')




  var upload = function(files){
    var formData = new FormData(),
      xhr = new XMLHttpRequest(),
      x;
      //Remove any previous image in gallery
    document.querySelector('.gallery').innerHTML = ''
    result.innerHTML = '';
    for(x = 0; x < files.length; x = x +1){
      formData.append('file[]', files[x])
      preview_image(files[x])
    }


    xhr.onload = function(){
      var data = this.responseText
      console.log(data)
      land_button.style.display = 'inline-block';
    }

    xhr.open('POST', '/');
    
    xhr.send(formData);
  }

  function preview_image(file){

    var reader = new FileReader();
    reader.onload = function(){
      var div = document.createElement('div');
      div.className = 'image_div'
      var image = document.createElement('img');
      image.src = reader.result
      image.className = 'image'
      div.appendChild(image)
      gallery.appendChild(div)
      console.log('Uploaded')
    }
  
    reader.readAsDataURL(file);
    
    
    
  }

  document.querySelector('.click_upload').onchange = function(e){
    upload(this.files)
  }

  default_upload.onclick = ()=>{
    console.log('Test')
   document.querySelector('.click_upload').click()   
  }


  dropzone.ondrop = function(e){
    e.preventDefault();
    this.className = 'dropzone'
    upload(e.dataTransfer.files)
    return false;
  };
  dropzone.ondragover = function(){
    this.className = 'dropzone dragover';
    return false;
  };

  dropzone.ondragleave = function(){
    this.className = 'dropzone';
    return false;
  }

  


  function detectLand(){
    xhr = new XMLHttpRequest();
    xhr.open('POST', '/detect')
    
    document.getElementById("loading").style.display = 'block';

    xhr.onload = ()=>{
      results = document.getElementsByClassName('image_result');
      if(results.length != 0){
        results[0].innerHTML = ''
      }
      var div = document.createElement('div');
      div.className = 'image_result'
      document.getElementById("loading").style.display = 'none';
      data = JSON.parse(xhr.response)
      console.log(data)
      for(d in data){

        console.log(data[d])  
        var image = document.createElement('img');
        image.src = data[d]
        image.className = 'land_images'
        div.appendChild(image)
        result.appendChild(div)
      }
      a = document.createElement('a');
      a.type = 'button'
      a.className = 'land_button';
      a.id = 'blueprint';
      a.innerHTML = 'Generate blueprint';
      a.href = '/blueprint'
      
      
      div.appendChild(a)
    }

    xhr.send()
  }

  land_button.onclick = ()=>{
    console.log('Workee')
    detectLand();
  }
});