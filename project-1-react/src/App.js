import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Arius Ulibarri</h1>
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Hello! Welcome to my about me page. My name is Arius, a current computer systems major with a minor in computer science on 
          his last semester of college (for now). You can look at my github profile 
          <a className="App-Link" href="https://github.com/Ulibomber1" target="_blank" rel="noopener noreferrer"> here.</a>
        </p>
        <h3>What I've Done</h3>
        <p>
          I have been programming for around 8 years now, with experience in several languages. First starting out I worked with BlitzMax BASIC, 
          but afterwards I slowly transitioned to using C and C++ in Visual Studio. I programmed primarily labs for my classes, and a few 
          Project Euler programming exercises for practice. Once I transferred here to CSUSB, I had started using Unity to develop video games 
          which required me to learn C# and the Unity scripting API. I have a few games I had a part in creating on Itch.io: MechroKnight and 
          Crystalpunk. I most recently learned to use the Godot game engine as well, which can also use C# as a scripting language. I have no 
          games made in the engine yet, but I am slowly learning how to use it.
        </p>
        <h3>What I'm Doing Next</h3>
        <p>
          I am set to graduate soon, so I am currently looking for career opportunities in the software engineering and game programming fields. 
          At the same time, once I have graduated I will also be working on my portfolio of programming projects and compiling them together on 
          my own website and on LinkedIn, Discord, etc. 
        </p>
        <h3>Hobbies & Interests</h3>
        <ul>
          <li>Video & Tabletop Games</li>
          <li>Bike rides</li>
          <li>Gunpla & mecha!!</li>
          <li>Anime & anime-adjacent media</li>
          <li>Anything computer programming-related</li>
          <li>My cat, Cleo (down below)</li>
        </ul>
        <img src="IMG_4442.jpeg" alt="Cleo"></img>
      </header>
    </div>
  );
}

export default App;
