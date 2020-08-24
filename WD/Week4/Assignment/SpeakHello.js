(function (window) {
    var helloSpeaker = new Object;
    helloSpeaker.speak = function(name) {
        console.log(speakWord + " " + name);
    }

    var speakWord = "Hello";

    window.helloSpeaker = helloSpeaker;
})(window);