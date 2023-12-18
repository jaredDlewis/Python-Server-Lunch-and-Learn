let prevClassesArr = new Array(20).fill('');

const toggleClasses = () => {
  const headings = Array.from(document.querySelectorAll('h1'));
  const button = document.querySelector('button');

  const currClassesArr = headings.map((heading, idx) => {
    const currClass = heading.className;
    heading.className = prevClassesArr[idx];
    return currClass;
  });
  prevClassesArr = currClassesArr;
  button.innerText = (button.innerText === 'STOP THE BLINKING') ? 'Restart the Blinking': 'STOP THE BLINKING';
};

const createButton = () => {
  const div = document.querySelector('div');
  const button = document.createElement('button');
  button.addEventListener('click', toggleClasses);
  button.innerText = 'STOP THE BLINKING';
  div.appendChild(button);
};

document.addEventListener("DOMContentLoaded", () => {
  createButton();
});
