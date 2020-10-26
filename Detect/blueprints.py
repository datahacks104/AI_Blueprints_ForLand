import pyautogui
import time
import webbrowser
import cv2
import keyboard

def web3():
    html_str = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <meta http-equiv="X-UA-Compatible" content="ie=edge">
      <title>Canvas Drawing App</title>
      <link rel="stylesheet" href="assets/css/main.min.css" />
    </head>
    <body>
    <script>
    window.alert("Please don't move course during map plotting");
</script>

      <canvas></canvas>
      <main>
      <script>
    window.alert("Please don't move course during map plotting");
</script>
     <!--  3- Marla lable  -->

            <pre class="bed"> Bedroom                               Laundary                                 Bedroom </pre>
            <pre class="tv">TV Lounge                                                           Kitchen</pre>
            <pre class="l">                  Garage                                        dining room            bathroom</pre>




    <style>

        .bed
        {
        margin-left: 450px;
       margin-top: 100px;
       color: blue;
       font-size: 10px;
        }
         .tv
        {
        margin-left: 600px;
       margin-top: 200px;
       color: blue;
       font-size: 10px;
        }
        .l
        {
        margin-left: 500px;
       margin-top: 230px;
       color: blue;
       font-size: 10px;
        }


    </style>

          <section class="colors">
            <input type="text" class="color-picker" value="#171717" />
          </section>
          <section class="thickness">
            <input type="number" class="stroke-weight" value="3" />
          </section>
          <button class="clear">X</button>f
          <br>
          <section class="colors clear">
            <button class="clear" style="background-color: aqua;">T</button>
            <input style="font-size: 35px; font-family: Georgia, 'Times New Roman', Times, serif ; width: auto;" type="text" class="color-picker"/>
          </section>





      </main>
      <script src="assets/js/main.js"></script>


    </body>
    </html>
    """

    Html_file = open("index.html", "w")
    Html_file.write(html_str)
    Html_file.close()
    url = 'file://C:/Users/World/Desktop/Detect/index.html'
    webbrowser.open(url, new=1)


def web5():
    html_str = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <meta http-equiv="X-UA-Compatible" content="ie=edge">
      <title>Canvas Drawing App</title>
      <link rel="stylesheet" href="assets/css/main.min.css" />
    </head>
    <body>

      <canvas></canvas>
      <main>
      <script>
    window.alert("Please don't move course during map plotting");
</script>
    
               <!--  5- Marla -->
           <pre class="dr">  Bathroom                                               Bathroom </pre>
            <pre class="bed"> Bedroom                              Laundary                               Bedroom </pre>
            <pre class="tv">TV Lounge                                                           Kitchen</pre>
            <pre class="l">                  Garage                                        dining room            bathroom</pre>




    <style>
        .dr
        {
        margin-left: 550px;
       margin-top: 10px;
       color: blue;
       font-size: 10px;
        }
        .bed
        {
        margin-left: 450px;
       margin-top: 100px;
       color: blue;
       font-size: 10px;
        }
         .tv
        {
        margin-left: 600px;
       margin-top: 200px;
       color: blue;
       font-size: 10px;
        }
        .l
        {
        margin-left: 500px;
       margin-top: 230px;
       color: blue;
       font-size: 10px;
        }


    </style>


            

          <section class="colors">
            <input type="text" class="color-picker" value="#171717" />
          </section>
          <section class="thickness">
            <input type="number" class="stroke-weight" value="3" />
          </section>
          <button class="clear">X</button>f
          <br>
          <section class="colors clear">
            <button class="clear" style="background-color: aqua;">T</button>
            <input style="font-size: 35px; font-family: Georgia, 'Times New Roman', Times, serif ; width: auto;" type="text" class="color-picker"/>
          </section>





      </main>
      <script src="assets/js/main.js"></script>


    </body>
    </html>
    """

    Html_file = open("index.html", "w")
    Html_file.write(html_str)
    Html_file.close()
    url = 'file://F:/Land Detection/Detect/index.html'
    webbrowser.open(url, new=1)


def web5():
    html_str = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <meta http-equiv="X-UA-Compatible" content="ie=edge">
      <title>Canvas Drawing App</title>
      <link rel="stylesheet" href="assets/css/main.min.css" />
    </head>
    <body>

      <canvas></canvas>
      <main>
      <script>
    window.alert("Please don't move course during map plotting");
</script>

               <!--  5- Marla -->
           <pre class="dr">  Bathroom                                               Bathroom </pre>
            <pre class="bed"> Bedroom                              Laundary                               Bedroom </pre>
            <pre class="tv">TV Lounge                                                           Kitchen</pre>
            <pre class="l">                  Garage                                        dining room            bathroom</pre>




    <style>
        .dr
        {
        margin-left: 550px;
       margin-top: 10px;
       color: blue;
       font-size: 10px;
        }
        .bed
        {
        margin-left: 450px;
       margin-top: 100px;
       color: blue;
       font-size: 10px;
        }
         .tv
        {
        margin-left: 600px;
       margin-top: 200px;
       color: blue;
       font-size: 10px;
        }
        .l
        {
        margin-left: 500px;
       margin-top: 230px;
       color: blue;
       font-size: 10px;
        }


    </style>
          <section class="colors">
            <input type="text" class="color-picker" value="#171717" />
          </section>
          <section class="thickness">
            <input type="number" class="stroke-weight" value="3" />
          </section>
          <button class="clear">X</button>f
          <br>
          <section class="colors clear">
            <button class="clear" style="background-color: aqua;">T</button>
            <input style="font-size: 35px; font-family: Georgia, 'Times New Roman', Times, serif ; width: auto;" type="text" class="color-picker"/>
          </section>





      </main>
      <script src="assets/js/main.js"></script>


    </body>
    </html>
    """

    Html_file = open("index.html", "w")
    Html_file.write(html_str)
    Html_file.close()
    url = 'file://C:/Users/World/Desktop/Detect/index.html'
    webbrowser.open(url, new=1)


def web7():
    html_str = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <meta http-equiv="X-UA-Compatible" content="ie=edge">
      <title>Canvas Drawing App</title>
      <link rel="stylesheet" href="assets/css/main.min.css" />
    </head>
    <body>

      <canvas></canvas>
      <main>
      <script>
    window.alert("Please don't move course during map plotting");
</script>

        


            <!--  7- Marla  -->
           <pre class="dr">  Bathroom          Bathroom                                                   Bathroom </pre>
            <pre class="bed"> Bedroom                              Laundary                               Bedroom </pre>
            <pre class="tv">TV Lounge                                                           Kitchen</pre>
            <pre class="l">Lown                        Garage                                  dining room            bathroom</pre>




    <style>
        .dr
        {
        margin-left: 430px;
       margin-top: 10px;
       color: blue;
       font-size: 10px;
        }
        .bed
        {
        margin-left: 450px;
       margin-top: 100px;
       color: blue;
       font-size: 10px;
        }
         .tv
        {
        margin-left: 600px;
       margin-top: 200px;
       color: blue;
       font-size: 10px;
        }
        .l
        {
        margin-left: 500px;
       margin-top: 230px;
       color: blue;
       font-size: 10px;
        }


    </style>


          <section class="colors">
            <input type="text" class="color-picker" value="#171717" />
          </section>
          <section class="thickness">
            <input type="number" class="stroke-weight" value="3" />
          </section>
          <button class="clear">X</button>f
          <br>
          <section class="colors clear">
            <button class="clear" style="background-color: aqua;">T</button>
            <input style="font-size: 35px; font-family: Georgia, 'Times New Roman', Times, serif ; width: auto;" type="text" class="color-picker"/>
          </section>





      </main>
      <script src="assets/js/main.js"></script>


    </body>
    </html>
    """

    Html_file = open("index.html", "w")
    Html_file.write(html_str)
    Html_file.close()
    url = 'file://C:/Users/World/Desktop/Detect/index.html'
    webbrowser.open(url, new=1)


def web10():
    html_str = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <meta http-equiv="X-UA-Compatible" content="ie=edge">
      <title>Canvas Drawing App</title>
      <link rel="stylesheet" href="assets/css/main.min.css" />
    </head>
    <body>
    <script>
    window.alert("Please don't move course during map plotting");
</script>

      <canvas></canvas>
      <main>




         
             <!--    10- Marla -->
           <pre class="dr">  Bathroom          Bathroom                                                Bathroom </pre>
            <pre class="bed"> Bedroom     Bedroom                      Laundary                          Bedroom </pre>
            <pre class="tv">TV Lounge                                                           Kitchen</pre>
            <pre class="l">Lown                        Garage                                  dining room              bathroom</pre>




    <style>
        .dr
        {
        margin-left: 430px;
       margin-top: 10px;
       color: blue;
       font-size: 10px;
        }
        .bed
        {
        margin-left: 450px;
       margin-top: 70px;
       color: blue;
       font-size: 10px;
        }
         .tv
        {
        margin-left: 600px;
       margin-top: 200px;
       color: blue;
       font-size: 10px;
        }
        .l
        {
        margin-left: 500px;
       margin-top: 170px;
       color: blue;
       font-size: 10px;
        }


    </style>
          <section class="colors">
            <input type="text" class="color-picker" value="#171717" />
          </section>
          <section class="thickness">
            <input type="number" class="stroke-weight" value="3" />
          </section>
          <button class="clear">X</button>f
          <br>
          <section class="colors clear">
            <button class="clear" style="background-color: aqua;">T</button>
            <input style="font-size: 35px; font-family: Georgia, 'Times New Roman', Times, serif ; width: auto;" type="text" class="color-picker"/>
          </section>





      </main>
      <script src="assets/js/main.js"></script>


    </body>
    </html>
    """

    Html_file = open("index.html", "w")
    Html_file.write(html_str)
    Html_file.close()
    url = 'file://C:/Users/World/Desktop/Detect/index.html'
    webbrowser.open(url, new=1)


def web1Kanal():
    html_str = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <meta http-equiv="X-UA-Compatible" content="ie=edge">
      <title>Canvas Drawing App</title>
      <link rel="stylesheet" href="assets/css/main.min.css" />
    </head>
    <body>
   

      <canvas></canvas>
      <main>
       <script>
    window.alert("Please don't move course during map plotting");
</script>
          <!--        1- kanal  -->
           <pre class="dr">  Bathroom          Bathroom                                                Bathroom                    Bathroom</pre>
            <pre class="bed"> Bedroom     Bedroom                      Laundary                          Bedroom                Bedroom </pre>
            <pre class="tv">TV Lounge                                                           Kitchen</pre>
            <pre class="l">Lown                        Garage                                  dining room              bathroom</pre>
            <pre class="g">Gallery</pre>



    <style>
        .dr
        {
        margin-left: 450px;
       margin-top: 40px;
       color: blue;
       font-size: 10px;
        }
        .bed
        {
        margin-left: 450px;
       margin-top: 70px;
       color: blue;
       font-size: 10px;
        }
         .tv
        {
        margin-left: 600px;
       margin-top: 200px;
       color: blue;
       font-size: 10px;
        }
        .l
        {
        margin-left: 500px;
       margin-top: 200px;
       color: blue;
       font-size: 10px;
        }
        .g
        {
        margin-left: 700px;
       margin-top: 35px;
       color: blue;
       font-size: 10px;
        }

    </style>

          <section class="colors">
            <input type="text" class="color-picker" value="#171717" />
          </section>
          <section class="thickness">
            <input type="number" class="stroke-weight" value="3" />
          </section>
          <button class="clear">X</button>f
          <br>
          <section class="colors clear">
            <button class="clear" style="background-color: aqua;">T</button>
            <input style="font-size: 35px; font-family: Georgia, 'Times New Roman', Times, serif ; width: auto;" type="text" class="color-picker"/>
          </section>





      </main>
      <script src="assets/js/main.js"></script>


    </body>
    </html>
    """

    Html_file = open("index.html", "w")
    Html_file.write(html_str)
    Html_file.close()
    url = 'file://C:/Users/World/Desktop/Detect/index.html'
    webbrowser.open(url, new=1)


"""
    Three_Marla blueprint X:  438 Y:   76 RGB: (243, 243, 243)
    Drawing_Room 838, 497
    DiningBath_Horizontal 969, 607
    Garage 446,498
    Tv.Lounge 446,327
    kitchen 840, 327
    Bed 1: 600,80
    Bed 2: 861,81
    BedroomBath_UpperLine 601, 164
    BedroomBath_DownwardLine 601, 247 
    """
def three_marla():
    time.sleep(10)
    pyautogui.click()
    pyautogui.moveTo(438, 76, duration=0.3)
    distance = 600
    while distance > 0:
        pyautogui.drag(distance, 0, duration=5)  # move right
        distance = distance - 5
        pyautogui.drag(0, distance, duration=5)  # move down
        pyautogui.drag(-distance, 0, duration=5)  # move left
        distance = distance - 5
        pyautogui.drag(0, -distance, duration=5)  # move upwards
        break
    # Moving cursor inside the blueprint
    pyautogui.moveTo(446, 498, duration=0.3)  # Garage
    pyautogui.drag(600, 0, duration=4)

    pyautogui.drag(0, 171, duration=4)
    pyautogui.moveTo(969, 607, duration=0.3)  # DiningBath_Horizontal
    pyautogui.drag(68, 0, duration=4)
    pyautogui.moveTo(969, 607, duration=0.3)  # DiningBath_vertica
    pyautogui.drag(0, 65, duration=4)
    pyautogui.moveTo(446, 327, duration=0.3)  # T.V Lounge
    pyautogui.drag(595, 0, duration=4)
    pyautogui.moveTo(838, 497, duration=0.3)  # Dining
    pyautogui.moveTo(840, 327, duration=0.3)  # Kitchen
    pyautogui.drag(0, 171, duration=4)

    pyautogui.moveTo(600, 80, duration=0.3)  # Bedroom 1
    pyautogui.drag(0, 248, duration=4)

    pyautogui.moveTo(861, 81, duration=0.3)  # Bedroom2
    pyautogui.drag(0, 248, duration=4)
    pyautogui.moveTo(601, 164, duration=0.3)  # BedroomBath_UpperLine
    pyautogui.drag(261, 0, duration=4)

    pyautogui.moveTo(601, 247, duration=0.3)  # BedroomBath_DownwardLine
    pyautogui.drag(261, 0, duration=4)


#three_marla()

def five_marla():
    time.sleep(10)
    pyautogui.click()
    pyautogui.moveTo(438, 76, duration=0.3)
    distance = 600
    while distance > 0:
        pyautogui.drag(distance, 0, duration=5)  # move right
        distance = distance - 5
        pyautogui.drag(0, distance, duration=5)  # move down
        pyautogui.drag(-distance, 0, duration=5)  # move left
        distance = distance - 5
        pyautogui.drag(0, -distance, duration=5)  # move upwards
        break

    # Moving cursor inside the blueprint
    pyautogui.moveTo(446, 498, duration=0.3)  # Garage
    pyautogui.drag(600, 0, duration=4)

    pyautogui.moveTo(838, 497, duration=0.3)  # Dining
    pyautogui.drag(0, 171, duration=4)

    pyautogui.moveTo(969, 607, duration=0.3)  # DiningBath_Horizontal
    pyautogui.drag(68, 0, duration=4)

    pyautogui.moveTo(969, 607, duration=0.3)  # DiningBath_vertical
    pyautogui.drag(0, 65, duration=4)

    pyautogui.moveTo(446, 327, duration=0.3)  # T.V Lounge
    pyautogui.drag(595, 0, duration=4)

    pyautogui.moveTo(840, 327, duration=0.3)  # Kitchen
    pyautogui.drag(0, 171, duration=4)

    pyautogui.moveTo(600, 80, duration=0.3)  # Bedroom 1
    pyautogui.drag(0, 248, duration=4)

    pyautogui.moveTo(553, 136, duration=0.3)  # Bedroom 1_Bath_vertical
    pyautogui.drag(0, -61, duration=4)

    pyautogui.moveTo(553, 136, duration=0.3)  # Bedroom 1_Bath_horizontal
    pyautogui.drag(48, 0, duration=4)

    pyautogui.moveTo(861, 81, duration=0.3)  # Bedroom2
    pyautogui.drag(0, 248, duration=4)

    pyautogui.moveTo(910, 138, duration=0.3)  # Bedroom 2_Bath_vertical
    pyautogui.drag(0, -62, duration=4)

    pyautogui.moveTo(910, 138, duration=0.3)  # Bedroom 2_Bath_horizontal
    pyautogui.drag(-48, 0, duration=4)

    pyautogui.moveTo(601, 164, duration=0.3)  # Laundry_UpperLine
    pyautogui.drag(261, 0, duration=4)

    pyautogui.moveTo(601, 247, duration=0.3)  # Laundry_DownwardLine
    pyautogui.drag(261, 0, duration=4)

#five_marla()

def seven_marla():
    time.sleep(10)
    pyautogui.click()
    pyautogui.moveTo(438, 76, duration=0.3)
    distance = 600
    while distance > 0:
        pyautogui.drag(distance, 0, duration=5)  # move right
        distance = distance - 5
        pyautogui.drag(0, distance, duration=5)  # move down
        pyautogui.drag(-distance, 0, duration=5)  # move left
        distance = distance - 5
        pyautogui.drag(0, -distance, duration=5)  # move upwards
        break

    # Moving cursor inside the blueprint
    pyautogui.moveTo(446, 498, duration=0.3)  # Garage
    pyautogui.drag(600, 0, duration=4)

    pyautogui.moveTo(620, 498, duration=0.3)  # Porch
    pyautogui.drag(0, 171, duration=4)

    pyautogui.moveTo(838, 497, duration=0.3)  # Dining
    pyautogui.drag(0, 171, duration=4)

    pyautogui.moveTo(969, 607, duration=0.3)  # DiningBath_Horizontal
    pyautogui.drag(68, 0, duration=4)

    pyautogui.moveTo(969, 607, duration=0.3)  # DiningBath_vertical
    pyautogui.drag(0, 65, duration=4)

    pyautogui.moveTo(446, 327, duration=0.3)  # T.V Lounge
    pyautogui.drag(595, 0, duration=4)

    pyautogui.moveTo(840, 327, duration=0.3)  # Kitchen
    pyautogui.drag(0, 171, duration=4)

    pyautogui.moveTo(600, 80, duration=0.3)  # Bedroom 1
    pyautogui.drag(0, 248, duration=4)

    pyautogui.moveTo(553, 136, duration=0.3)  # Bedroom 1_Bath_vertical
    pyautogui.drag(0, -61, duration=4)

    pyautogui.moveTo(553, 136, duration=0.3)  # Bedroom 1_Bath_horizontal
    pyautogui.drag(48, 0, duration=4)

    pyautogui.moveTo(861, 81, duration=0.3)  # Bedroom2
    pyautogui.drag(0, 248, duration=4)

    pyautogui.moveTo(910, 138, duration=0.3)  # Bedroom 2_Bath_vertical
    pyautogui.drag(0, -62, duration=4)

    pyautogui.moveTo(910, 138, duration=0.3)  # Bedroom 2_Bath_horizontal
    pyautogui.drag(-48, 0, duration=4)

    pyautogui.moveTo(601, 164, duration=0.3)  # Laundry_UpperLine
    pyautogui.drag(261, 0, duration=4)

    pyautogui.moveTo(601, 247, duration=0.3)  # Laundry_DownwardLine
    pyautogui.drag(261, 0, duration=4)

#seven_marla()

def ten_marla():
    time.sleep(10)
    pyautogui.click()
    pyautogui.moveTo(438, 76, duration=0.3)
    distance = 600
    while distance > 0:
        pyautogui.drag(distance, 0, duration=5)  # move right
        distance = distance - 5
        pyautogui.drag(0, distance, duration=5)  # move down
        pyautogui.drag(-distance, 0, duration=5)  # move left
        distance = distance - 5
        pyautogui.drag(0, -distance, duration=5)  # move upwards
        break

    # Moving cursor inside the blueprint
    pyautogui.moveTo(446, 498, duration=0.3)  # Garage
    pyautogui.drag(600, 0, duration=4)

    pyautogui.moveTo(620, 498, duration=0.3)  # Porch
    pyautogui.drag(0, 171, duration=4)

    pyautogui.moveTo(838, 497, duration=0.3)  # Dining
    pyautogui.drag(0, 171, duration=4)

    pyautogui.moveTo(969, 607, duration=0.3)  # DiningBath_Horizontal
    pyautogui.drag(68, 0, duration=4)

    pyautogui.moveTo(969, 607, duration=0.3)  # DiningBath_vertical
    pyautogui.drag(0, 65, duration=4)

    pyautogui.moveTo(446, 327, duration=0.3)  # T.V Lounge
    pyautogui.drag(595, 0, duration=4)

    pyautogui.moveTo(840, 327, duration=0.3)  # Kitchen
    pyautogui.drag(0, 171, duration=4)

    pyautogui.moveTo(600, 80, duration=0.3)  # left_Bedroom 1
    pyautogui.drag(0, 248, duration=4)

    pyautogui.moveTo(553, 136, duration=0.3)  # left_Bedroom 1_Bath_vertical
    pyautogui.drag(0, -61, duration=4)

    pyautogui.moveTo(553, 136, duration=0.3)  # left_Bedroom 1_Bath_horizontal
    pyautogui.drag(48, 0, duration=4)

    pyautogui.moveTo(518, 80, duration=0.3)  # left_Bedroom 2
    pyautogui.drag(0, 248, duration=4)

    pyautogui.moveTo(475, 133, duration=0.3)  # left_Bedroom 2_Bath_vertical
    pyautogui.drag(0, -54.5, duration=4)

    pyautogui.moveTo(475, 133, duration=0.3)  # left_Bedroom 2_Bath_horizontal
    pyautogui.drag(-33, 0, duration=4)

    pyautogui.moveTo(861, 81, duration=0.3)  # right_Bedroom1
    pyautogui.drag(0, 248, duration=4)

    pyautogui.moveTo(910, 138, duration=0.3)  # right_Bedroom 1_Bath_vertical
    pyautogui.drag(0, -62, duration=4)

    pyautogui.moveTo(910, 138, duration=0.3)  # right_Bedroom 1_Bath_horizontal
    pyautogui.drag(-48, 0, duration=4)

    pyautogui.moveTo(601, 164, duration=0.3)  # Laundry_UpperLine
    pyautogui.drag(261, 0, duration=4)

    pyautogui.moveTo(601, 247, duration=0.3)  # Laundry_DownwardLine
    pyautogui.drag(261, 0, duration=4)

#ten_marla()

def one_kanal():
    time.sleep(10)
    pyautogui.click()
    pyautogui.moveTo(438, 76, duration=0.3)
    distance = 640
    while distance >= 610:
        pyautogui.drag(distance, 0, duration=5)  # move right
        distance = distance - 15
        pyautogui.drag(0, distance, duration=5)  # move down
        pyautogui.drag(-distance, 0, duration=5)  # move left
        distance = distance - 15
        pyautogui.drag(0, -distance, duration=5)  # move upwards

    # Moving cursor inside the blueprint
    pyautogui.moveTo(470, 498, duration=0.3)  # Garage
    pyautogui.drag(600, 0, duration=4)

    pyautogui.moveTo(620, 498, duration=0.3)  # Porch
    pyautogui.drag(0, 188, duration=4)

    pyautogui.moveTo(838, 497, duration=0.3)  # Dining
    pyautogui.drag(0, 188, duration=4)

    pyautogui.moveTo(998, 607, duration=0.3)  # DiningBath_Horizontal
    pyautogui.drag(65, 0, duration=4)

    pyautogui.moveTo(998, 607, duration=0.3)  # DiningBath_vertical
    pyautogui.drag(0, 80, duration=4)

    pyautogui.moveTo(470, 327, duration=0.3)  # T.V Lounge
    pyautogui.drag(600, 0, duration=4)

    pyautogui.moveTo(840, 327, duration=0.3)  # Kitchen
    pyautogui.drag(0, 173, duration=4)

    pyautogui.moveTo(600, 92, duration=0.3)  # left_Bedroom 1
    pyautogui.drag(0, 235, duration=4)

    pyautogui.moveTo(553, 136, duration=0.3)  # left_Bedroom 1_Bath_vertical
    pyautogui.drag(0, -45, duration=4)

    pyautogui.moveTo(553, 136, duration=0.3)  # left_Bedroom 1_Bath_horizontal
    pyautogui.drag(46, 0, duration=4)

    pyautogui.moveTo(517, 91, duration=0.3)  # left_Bedroom 2
    pyautogui.drag(0, 235, duration=4)

    pyautogui.moveTo(488, 131, duration=0.3)  # left_Bedroom 2_Bath_vertical
    pyautogui.drag(0, -40, duration=4)

    pyautogui.moveTo(488, 131, duration=0.3)  # left_Bedroom 2_Bath_horizontal
    pyautogui.drag(-18, 0, duration=4)

    pyautogui.moveTo(860, 91, duration=0.3)  # right_Bedroom1
    pyautogui.drag(0, 235, duration=4)

    pyautogui.moveTo(910, 138, duration=0.3)  # right_Bedroom 1_Bath_vertical
    pyautogui.drag(0, -45, duration=4)

    pyautogui.moveTo(910, 138, duration=0.3)  # right_Bedroom 1_Bath_horizontal
    pyautogui.drag(-50, 0, duration=4)

    pyautogui.moveTo(966, 91, duration=0.3)  # right_Bedroom2
    pyautogui.drag(0, 235, duration=4)

    pyautogui.moveTo(1016, 135, duration=0.3)  # right_Bedroom 2_Bath_vertical
    pyautogui.drag(0, -44, duration=4)

    pyautogui.moveTo(1016, 135, duration=0.3)  # right_Bedroom 2_Bath_horizontal
    pyautogui.drag(47, 0, duration=4)

    pyautogui.moveTo(601, 164, duration=0.3)  # Laundry_UpperLine
    pyautogui.drag(261, 0, duration=4)

    pyautogui.moveTo(601, 247, duration=0.3)  # Laundry_DownwardLine
    pyautogui.drag(261, 0, duration=4)

#one_kanal()
