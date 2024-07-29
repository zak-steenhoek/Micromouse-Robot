<a id="readme-top"></a>



<!-- PROJECT SHIELDS -->

[![Contributors][contributors-shield]][contributors-url]
[![Acknowledgments][acknowledgments-shield]][acknowledgments-url]
[![Stars][stars-shield]][stars-url]
[![Forks][forks-shield]][forks-url]

[![Dependencies][dependencies-shield]][dependencies-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]



<!-- PROJECT TITLE -->

<h1 align="center">Micromouse Robot</h1>



<!-- PROJECT DESCRIPTION -->

  <p align="center">
    A program to guide an autonomous robot to the center of an unknown maze using a variation of the floodfill algorithm.
    <br />
    <br />
    <a href="https://github.com/zak-steenhoek/Micromouse-Robot/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    ⋅
    <a href="https://github.com/zak-steenhoek/Micromouse-Robot/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
    </li>
    <li><a href="#contributions">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->

## About The Project

This was my final project for my 'Introduction to Autonomous Vehicle Systems' class, which I took in the Spring of 2024 in my fourth semester. 
My team and I decided to create a replica micromouse robot: an autonomous robot meant to solve the path through a maze previously unknown and 
execute it with the quickest time. This is an established concept, with competitions held between robotics teams under common design requirements. 
You can find more about the official robots at the [Micromouse USA](http://micromouseusa.com/) website.

With this in mind, we set out to build our own version. We immediately began research on other sucessful mms teams, different pathfinding algorithms, hardware
requirements, and more. We decided to use a variation of the [floodfill algorithm](https://en.wikipedia.org/wiki/Flood_fill), which is commonly used in 
things like the fill tool found in many editing applications. The variation comes from the fact that there are walls, and we don't know where they are 
yet. To this end, we must have hardware that supports wall detection. One other thing we uncovered in our research, unfortunately, is that high quality 
electronics and robotics parts are _not_ cheap (foreshadowing!). We elected to use ultrasonic sensors for our wall detection, which would give us the data
we needed to support our pathfinding algorithm. 

Once we had the rest of our hardware selected, we got to the software side of things. The project required both a prototype _and_ and simulation, which meant
more than just programming an Arduino. We uncovered a Github repo which, conviently enough, contained an autonomous robot simulator. At this point, I decided 
to take up the bulk of the software workload. After some brutal trial and error I got the simulation environment setup and responsive to a basic left-wall
follower program. The simulator could be downloaded to support many different languages, and I chose Python. At this point, it was just a matter of writing 
the program to utilize a variation of floodfill to determine the quickest path to the center of the maze. 


<p align="right">(<a href="#readme-top">^</a>)</p>



<!-- BUILT WITH -->

## Built With

&nbsp;&nbsp;&nbsp;&nbsp;[![Python][python-shield]][python-url]


<p align="right">(<a href="#readme-top">^</a>)</p>



<!-- GETTING STARTED -->

## Getting Started

To get a local copy up and running, follow these steps...

* Download the [mms sim](https://github.com/zak-steenhoek/Micromouse-Robot/blob/main/ref/mms-repo) in the language of your choice. I chose python, but many other options are available.

* Setup your simulator. Instructions can be found in the mms repo linked above. Some example mazes can be found [here](https://github.com/zak-steenhoek/Micromouse-Robot/blob/main/mazes)

* Start writing your program! 

<p align="right">(<a href="#readme-top">^</a>)</p>



<!-- ACKNOWLEDGMENTS -->

## Acknowledgments

* Creators of the Micromouse simulator
* Creators of the piccola project

<p align="right">(<a href="#readme-top">^</a>)</p>



<!-- CONTRIBUTIONS -->

## Contributions

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">^</a>)</p>



<!-- LICENSE -->

## License

Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#readme-top">^</a>)</p>



<!-- CONTACT -->

## Contact  

* Author: Zakary Steenhoek

* Project Link: [https://github.com/zak-steenhoek/Micromouse-Robot](https://github.com/zak-steenhoek/Micromouse-Robot)

[![Email][email-shield]][email-url]
[![LinkedIn][linkedin-shield]][linkedin-url]
[![Instagram][ig-shield]][ig-url]

<p align="right">(<a href="#readme-top">^</a>)</p>




<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->


<!-- BADGES -->
[contributors-shield]: https://img.shields.io/badge/-Contributors-black.svg?logoSize=auto&style=for-the-badge&logo=codementor&logoColor=D7CFB7&labelColor=463C1E&color=463C1E
[contributors-url]: https://github.com/zak-steenhoek/Micromouse-Robot/blob/main/ref

[forks-shield]: https://img.shields.io/badge/-Forks-black.svg?logoSize=auto&style=for-the-badge&logo=greasyfork&logoColor=D7CFB7&labelColor=463C1E&color=463C1E
[forks-url]: https://github.com/zak-steenhoek/Micromouse-Robot/forks

[stars-shield]: https://img.shields.io/badge/-Stars-black.svg?logoSize=auto&style=for-the-badge&logo=airtransat&logoColor=D7CFB7&labelColor=463C1E&color=463C1E
[stars-url]: https://github.com/zak-steenhoek/Micromouse-Robot/stargazers

[issues-shield]: https://img.shields.io/badge/-Issues-black.svg?logoSize=auto&style=for-the-badge&logo=gnometerminal&logoColor=D7CFB7&labelColor=463C1E&color=463C1E
[issues-url]: https://github.com/zak-steenhoek/Micromouse-Robot/issues

[dependencies-shield]: https://img.shields.io/badge/-Dependencies-black.svg?logoSize=auto&style=for-the-badge&logo=webmoney&logoColor=D7CFB7&labelColor=463C1E&color=463C1E
[dependencies-url]: https://github.com/zak-steenhoek/Micromouse-Robot/network/dependencies

[acknowledgments-shield]: https://img.shields.io/badge/-Acknowledgments-black.svg?logoSize=auto&style=for-the-badge&logo=elegoo&logoColor=D7CFB7&labelColor=463C1E&color=463C1E
[acknowledgments-url]: https://github.com/zak-steenhoek/Micromouse-Robot/blob/main/README.md#acknowledgments

[license-shield]: https://img.shields.io/badge/-Licence-black.svg?logoSize=auto&style=for-the-badge&logo=adblock&logoColor=D7CFB7&labelColor=463C1E&color=463C1E
[license-url]: https://github.com/zak-steenhoek/Micromouse-Robot/blob/main/LICENSE



<!-- MADE WITH -->
[python-shield]: https://img.shields.io/badge/-Python-black.svg?logoSize=auto&style=for-the-badge&logo=python&logoColor=D7CFB7&labelColor=463C1E&color=463C1E
[python-url]: https://www.python.org/

[cpp-shield]: https://img.shields.io/badge/-C++-black.svg?logoSize=auto&style=for-the-badge&logo=cplusplus&logoColor=D7CFB7&labelColor=463C1E&color=463C1E
[cpp-url]: https://cplusplus.com/

[bash-shield]: https://img.shields.io/badge/-GNU&nbsp;Bash-black.svg?logoSize=auto&style=for-the-badge&logo=gnubash&logoColor=D7CFB7&labelColor=463C1E&color=463C1E
[bash-url]: https://www.gnu.org/software/bash/

[npp-shield]: https://img.shields.io/badge/-Notepad++-black.svg?logoSize=auto&style=for-the-badge&logo=notepadplusplus&logoColor=D7CFB7&labelColor=463C1E&color=463C1E
[npp-url]: https://notepad-plus-plus.org/

[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/

[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/

[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/

[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/

[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/

[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com

[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com

[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 


<!-- CONTACT -->
[email-shield]: https://img.shields.io/badge/-Email-black.svg?logoSize=auto&style=for-the-badge&logo=gmail&logoColor=D7CFB7&labelColor=463C1E&color=463C1E
[email-url]: zasteenhoek@gmail.com

[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?logoSize=auto&style=for-the-badge&logo=linkedin&logoColor=D7CFB7&labelColor=463C1E&color=463C1E
[linkedin-url]: https://linkedin.com/in/zakary-steenhoek-aerospace-engineering-student/

[ig-shield]: https://img.shields.io/badge/-Instagram-black.svg?logoSize=auto&style=for-the-badge&logo=instagram&logoColor=D7CFB7&labelColor=463C1E&color=463C1E
[ig-url]: https://www.instagram.com/zak.steenhoek/
