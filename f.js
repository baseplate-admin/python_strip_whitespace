
() => {
    switch (button_turned) {
        case true : {
            anime({
                targets: '.animejs__facebook__button',
                translateX: 0,
                easing: 'easeOutSine',
                duration: 150,
                opacity: 1 ,
                scale: 1;            });            break;        };        case false: {
            anime({
                targets: '.animejs__facebook__button',
                translateX: 40 * 2,
                easing: 'easeOutSine',
                duration: 150,
                opacity: 0,
                scale: 0.2;            });            break;        };    };};