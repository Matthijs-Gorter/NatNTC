// video controlls
const video1 = document.getElementById("cWVideo");
const video2 = document.getElementById("bSVideo");

document.addEventListener("keydown", function (event) {
    if (event.code === "Comma") { // Handle "<" key press
        if (document.activeElement === video1) {
            event.preventDefault();
            video1.currentTime -= 1 / (30 * video1.playbackRate); // divide with 30 becuse 30 fps
        } else if (document.activeElement === video2) {
            event.preventDefault();
            video2.currentTime -= 1 / (30 * video2.playbackRate);
        }
    } else if (event.code === "Period") { // Handle ">" key press
        if (document.activeElement === video1) {
            event.preventDefault();
            video1.currentTime += 1 / (30 * video1.playbackRate);
        } else if (document.activeElement === video2) {
            event.preventDefault();
            video2.currentTime += 1 / (30 * video2.playbackRate);
        }
    } else if (event.key === "k" || event.code === "Space") { // Handle spacebar press
        if (document.activeElement === video1) {
            event.preventDefault();
            if (video1.paused) {
                video1.play();
            } else {
                video1.pause();
            }
        } else if (document.activeElement === video2) {
            event.preventDefault();
            if (video2.paused) {
                video2.play();
            } else {
                video2.pause();
            }
        }
    }
});

video1.addEventListener("click", function () {
    video1.focus();
});

video2.addEventListener("click", function () {
    video2.focus();
});


// Generate table of contents
document.addEventListener("DOMContentLoaded", function () {
  const tocContainer = document.getElementById("toc");
  const headings = document.querySelectorAll("h2, h3, h4, h5");
  const tocList = document.createElement("ul");
  let currentLevel = 2; // Starting level for the ToC
  let parentList = tocList; // Track the current parent list

  headings.forEach(function (heading) {
    const level = parseInt(heading.tagName[1]); // Extract the heading level (2 or 3)

    // Generate unique ID if the heading doesn't have one
    if (!heading.id) {
      heading.id = "heading-" + Math.random().toString(36).substr(2, 9);
    }

    const listItem = document.createElement("li");
    const link = document.createElement("a");
    link.textContent = heading.textContent;
    link.href = "#" + heading.id;
    
    // Apply styles to non-h2 headings
    if (level !== 2) {
      listItem.style = "margin-top: 0px;";
      link.style = "color: grey !important; font-size: 0.8rem;";
    }
    
    if (link.textContent != "Inhoud") {
      listItem.appendChild(link);
    }
    link.addEventListener("click", function (e) {
      e.preventDefault();
      const targetHeading = document.getElementById(heading.id);
      targetHeading.scrollIntoView({ behavior: "smooth" });
    });

    if (level > currentLevel) {
      const sublist = document.createElement("ul");
      sublist.appendChild(listItem);
      parentList.lastElementChild.appendChild(sublist);
      parentList = sublist; // Update the parent list reference
    } else if (level < currentLevel) {
      while (level < currentLevel) {
        parentList = parentList.parentElement.parentElement;
        currentLevel--;
      }
      parentList.appendChild(listItem);
    } else {
      parentList.appendChild(listItem);
    }

    currentLevel = level;
  });

  tocContainer.appendChild(tocList);
});


// don't scroll to the right
window.addEventListener("scroll", function () {
  if (window.scrollX > 0) {
    window.scrollTo(0, window.scrollY);
  }
});

// parallel scroll
window.addEventListener("scroll", function () {
  document.getElementById("header-img").style.transform =
    "translateY(" + -window.scrollY / 2 + "px)";
  document.getElementById("title").style.transform =
    "translate(-50%," + -window.scrollY / 3 + "px)";
  document.getElementById("info").style.transform =
    "translateY(" + -window.scrollY * 0.5 + "px)";
});
