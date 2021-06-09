var multiItemSlider = (function () {
  return function (selector, config) {
    var
      _mainElement = document.querySelector(selector), // основный элемент блока
      _sliderWrapper = _mainElement.querySelector('.slider__wrapper'), // обертка для .slider-item
      _sliderItems = _mainElement.querySelectorAll('.slider__item'), // элементы (.slider-item)
      _sliderControls = _mainElement.querySelectorAll('.slider__control'), // элементы управления
      _sliderControlLeft = _mainElement.querySelector('.slider__control_left'), // кнопка "LEFT"
      _sliderControlRight = _mainElement.querySelector('.slider__control_right'), // кнопка "RIGHT"
      _wrapperWidth = parseFloat(getComputedStyle(_sliderWrapper).width), // ширина обёртки
      _itemWidth = parseFloat(getComputedStyle(_sliderItems[0]).width), // ширина одного элемента
      _positionLeftItem = 0, // позиция левого активного элемента
      _transform = 0, // значение транфсофрмации .slider_wrapper
      _step = _itemWidth / _wrapperWidth * 100, // величина шага (для трансформации)
      _items = []; // массив элементов
    // наполнение массива _items
    _sliderItems.forEach(function (item, index) {
      _items.push({ item: item, position: index, transform: 0 });
    });

    var position = {
      getMin: 0,
      getMax: _items.length - 1
    };

    var _transformItem = function (direction) {
      if (direction === 'right') {
        if ((_positionLeftItem + _wrapperWidth / _itemWidth - 1) >= position.getMax) {
          return;
        }
        if (!_sliderControlLeft.classList.contains('slider__control_show')) {
          _sliderControlLeft.classList.add('slider__control_show');
        }
        if (_sliderControlRight.classList.contains('slider__control_show') && (_positionLeftItem + _wrapperWidth / _itemWidth) >= position.getMax) {
          _sliderControlRight.classList.remove('slider__control_show');
        }
        _positionLeftItem++;
        _transform -= _step;
      }
      if (direction === 'left') {
        if (_positionLeftItem <= position.getMin) {
          return;
        }
        if (!_sliderControlRight.classList.contains('slider__control_show')) {
          _sliderControlRight.classList.add('slider__control_show');
        }
        if (_sliderControlLeft.classList.contains('slider__control_show') && _positionLeftItem - 1 <= position.getMin) {
          _sliderControlLeft.classList.remove('slider__control_show');
        }
        _positionLeftItem--;
        _transform += _step;
      }
      _sliderWrapper.style.transform = 'translateX(' + _transform + '%)';
    };

    // обработчик события click для кнопок "назад" и "вперед"
    var _controlClick = function (e) {
      if (e.target.classList.contains('slider__control')) {
        e.preventDefault();
        var direction = e.target.classList.contains('slider__control_right') ? 'right' : 'left';
        _transformItem(direction);
      }
    };

    var _setUpListeners = function () {
      // добавление к кнопкам "назад" и "вперед" обрботчика _controlClick для событя click
      _sliderControls.forEach(function (item) {
        item.addEventListener('click', _controlClick);
      });
    };

    // инициализация
    _setUpListeners();

    return {
      right: function () { // метод right
        _transformItem('right');
      },
      left: function () { // метод left
        _transformItem('left');
      }
    }

  }
}());
var multiItemSlider2 = (function () {
  return function (selector, config) {
    var
      _mainElement = document.querySelector(selector), // основный элемент блока
      _sliderWrapper = _mainElement.querySelector('.slider__wrapper2'), // обертка для .slider-item
      _sliderItems = _mainElement.querySelectorAll('.slider__item2'), // элементы (.slider-item)
      _sliderControls = _mainElement.querySelectorAll('.slider__control2'), // элементы управления
      _sliderControlLeft = _mainElement.querySelector('.slider__control_left2'), // кнопка "LEFT"
      _sliderControlRight = _mainElement.querySelector('.slider__control_right2'), // кнопка "RIGHT"
      _wrapperWidth = parseFloat(getComputedStyle(_sliderWrapper).width), // ширина обёртки
      _itemWidth = parseFloat(getComputedStyle(_sliderItems[0]).width), // ширина одного элемента
      _positionLeftItem = 0, // позиция левого активного элемента
      _transform = 0, // значение транфсофрмации .slider_wrapper
      _step = _itemWidth / _wrapperWidth * 100, // величина шага (для трансформации)
      _items = []; // массив элементов
    // наполнение массива _items
    _sliderItems.forEach(function (item, index) {
      _items.push({ item: item, position: index, transform: 0 });
    });

    var position = {
      getMin: 0,
      getMax: _items.length - 1
    };

    var _transformItem = function (direction) {
      if (direction === 'right') {
        if ((_positionLeftItem + _wrapperWidth / _itemWidth - 1) >= position.getMax) {
          return;
        }
        if (!_sliderControlLeft.classList.contains('slider__control_show2')) {
          _sliderControlLeft.classList.add('slider__control_show2');
        }
        if (_sliderControlRight.classList.contains('slider__control_show2') && (_positionLeftItem + _wrapperWidth / _itemWidth) >= position.getMax) {
          _sliderControlRight.classList.remove('slider__control_show2');
        }
        _positionLeftItem++;
        _transform -= _step;
      }
      if (direction === 'left') {
        if (_positionLeftItem <= position.getMin) {
          return;
        }
        if (!_sliderControlRight.classList.contains('slider__control_show2')) {
          _sliderControlRight.classList.add('slider__control_show2');
        }
        if (_sliderControlLeft.classList.contains('slider__control_show2') && _positionLeftItem - 1 <= position.getMin) {
          _sliderControlLeft.classList.remove('slider__control_show2');
        }
        _positionLeftItem--;
        _transform += _step;
      }
      _sliderWrapper.style.transform = 'translateX(' + _transform + '%)';
    };

    // обработчик события click для кнопок "назад" и "вперед"
    var _controlClick = function (e) {
      if (e.target.classList.contains('slider__control2')) {
        e.preventDefault();
        var direction = e.target.classList.contains('slider__control_right2') ? 'right' : 'left';
        _transformItem(direction);
      }
    };

    var _setUpListeners = function () {
      // добавление к кнопкам "назад" и "вперед" обрботчика _controlClick для событя click
      _sliderControls.forEach(function (item) {
        item.addEventListener('click', _controlClick);
      });
    };

    // инициализация
    _setUpListeners();

    return {
      right: function () { // метод right
        _transformItem('right');
      },
      left: function () { // метод left
        _transformItem('left');
      }
    }

  }
}());
var multiItemSlider3 = (function () {
  return function (selector, config) {
    var
      _mainElement = document.querySelector(selector), // основный элемент блока
      _sliderWrapper = _mainElement.querySelector('.slider__wrapper3'), // обертка для .slider-item
      _sliderItems = _mainElement.querySelectorAll('.slider__item3'), // элементы (.slider-item)
      _sliderControls = _mainElement.querySelectorAll('.slider__control3'), // элементы управления
      _sliderControlLeft = _mainElement.querySelector('.slider__control_left3'), // кнопка "LEFT"
      _sliderControlRight = _mainElement.querySelector('.slider__control_right3'), // кнопка "RIGHT"
      _wrapperWidth = parseFloat(getComputedStyle(_sliderWrapper).width), // ширина обёртки
      _itemWidth = parseFloat(getComputedStyle(_sliderItems[0]).width), // ширина одного элемента
      _positionLeftItem = 0, // позиция левого активного элемента
      _transform = 0, // значение транфсофрмации .slider_wrapper
      _step = _itemWidth / _wrapperWidth * 100, // величина шага (для трансформации)
      _items = []; // массив элементов
    // наполнение массива _items
    _sliderItems.forEach(function (item, index) {
      _items.push({ item: item, position: index, transform: 0 });
    });

    var position = {
      getMin: 0,
      getMax: _items.length - 1
    };

    var _transformItem = function (direction) {
      if (direction === 'right') {
        if ((_positionLeftItem + _wrapperWidth / _itemWidth - 1) >= position.getMax) {
          return;
        }
        if (!_sliderControlLeft.classList.contains('slider__control_show3')) {
          _sliderControlLeft.classList.add('slider__control_show3');
        }
        if (_sliderControlRight.classList.contains('slider__control_show3') && (_positionLeftItem + _wrapperWidth / _itemWidth) >= position.getMax) {
          _sliderControlRight.classList.remove('slider__control_show3');
        }
        _positionLeftItem++;
        _transform -= _step;
      }
      if (direction === 'left') {
        if (_positionLeftItem <= position.getMin) {
          return;
        }
        if (!_sliderControlRight.classList.contains('slider__control_show3')) {
          _sliderControlRight.classList.add('slider__control_show3');
        }
        if (_sliderControlLeft.classList.contains('slider__control_show3') && _positionLeftItem - 1 <= position.getMin) {
          _sliderControlLeft.classList.remove('slider__control_show3');
        }
        _positionLeftItem--;
        _transform += _step;
      }
      _sliderWrapper.style.transform = 'translateX(' + _transform + '%)';
    };

    // обработчик события click для кнопок "назад" и "вперед"
    var _controlClick = function (e) {
      if (e.target.classList.contains('slider__control3')) {
        e.preventDefault();
        var direction = e.target.classList.contains('slider__control_right3') ? 'right' : 'left';
        _transformItem(direction);
      }
    };

    var _setUpListeners = function () {
      // добавление к кнопкам "назад" и "вперед" обрботчика _controlClick для событя click
      _sliderControls.forEach(function (item) {
        item.addEventListener('click', _controlClick);
      });
    };

    // инициализация
    _setUpListeners();

    return {
      right: function () { // метод right
        _transformItem('right');
      },
      left: function () { // метод left
        _transformItem('left');
      }
    }

  }
}());
var multiItemSlider4 = (function () {
  return function (selector, config) {
    var
      _mainElement = document.querySelector(selector), // основный элемент блока
      _sliderWrapper = _mainElement.querySelector('.slider__wrapper4'), // обертка для .slider-item
      _sliderItems = _mainElement.querySelectorAll('.slider__item4'), // элементы (.slider-item)
      _sliderControls = _mainElement.querySelectorAll('.slider__control4'), // элементы управления
      _sliderControlLeft = _mainElement.querySelector('.slider__control_left4'), // кнопка "LEFT"
      _sliderControlRight = _mainElement.querySelector('.slider__control_right4'), // кнопка "RIGHT"
      _wrapperWidth = parseFloat(getComputedStyle(_sliderWrapper).width), // ширина обёртки
      _itemWidth = parseFloat(getComputedStyle(_sliderItems[0]).width), // ширина одного элемента
      _positionLeftItem = 0, // позиция левого активного элемента
      _transform = 0, // значение транфсофрмации .slider_wrapper
      _step = _itemWidth / _wrapperWidth * 100, // величина шага (для трансформации)
      _items = []; // массив элементов
    // наполнение массива _items
    _sliderItems.forEach(function (item, index) {
      _items.push({ item: item, position: index, transform: 0 });
    });

    var position = {
      getMin: 0,
      getMax: _items.length - 1
    };

    var _transformItem = function (direction) {
      if (direction === 'right') {
        if ((_positionLeftItem + _wrapperWidth / _itemWidth - 1) >= position.getMax) {
          return;
        }
        if (!_sliderControlLeft.classList.contains('slider__control_show4')) {
          _sliderControlLeft.classList.add('slider__control_show4');
        }
        if (_sliderControlRight.classList.contains('slider__control_show4') && (_positionLeftItem + _wrapperWidth / _itemWidth) >= position.getMax) {
          _sliderControlRight.classList.remove('slider__control_show4');
        }
        _positionLeftItem++;
        _transform -= _step;
      }
      if (direction === 'left') {
        if (_positionLeftItem <= position.getMin) {
          return;
        }
        if (!_sliderControlRight.classList.contains('slider__control_show4')) {
          _sliderControlRight.classList.add('slider__control_show4');
        }
        if (_sliderControlLeft.classList.contains('slider__control_show4') && _positionLeftItem - 1 <= position.getMin) {
          _sliderControlLeft.classList.remove('slider__control_show4');
        }
        _positionLeftItem--;
        _transform += _step;
      }
      _sliderWrapper.style.transform = 'translateX(' + _transform + '%)';
    };

    // обработчик события click для кнопок "назад" и "вперед"
    var _controlClick = function (e) {
      if (e.target.classList.contains('slider__control4')) {
        e.preventDefault();
        var direction = e.target.classList.contains('slider__control_right4') ? 'right' : 'left';
        _transformItem(direction);
      }
    };

    var _setUpListeners = function () {
      // добавление к кнопкам "назад" и "вперед" обрботчика _controlClick для событя click
      _sliderControls.forEach(function (item) {
        item.addEventListener('click', _controlClick);
      });
    };

    // инициализация
    _setUpListeners();

    return {
      right: function () { // метод right
        _transformItem('right');
      },
      left: function () { // метод left
        _transformItem('left');
      }
    }

  }
}());
var multiItemSlider5 = (function () {
  return function (selector, config) {
    var
      _mainElement = document.querySelector(selector), // основный элемент блока
      _sliderWrapper = _mainElement.querySelector('.slider__wrapper5'), // обертка для .slider-item
      _sliderItems = _mainElement.querySelectorAll('.slider__item5'), // элементы (.slider-item)
      _sliderControls = _mainElement.querySelectorAll('.slider__control5'), // элементы управления
      _sliderControlLeft = _mainElement.querySelector('.slider__control_left5'), // кнопка "LEFT"
      _sliderControlRight = _mainElement.querySelector('.slider__control_right5'), // кнопка "RIGHT"
      _wrapperWidth = parseFloat(getComputedStyle(_sliderWrapper).width), // ширина обёртки
      _itemWidth = parseFloat(getComputedStyle(_sliderItems[0]).width), // ширина одного элемента
      _positionLeftItem = 0, // позиция левого активного элемента
      _transform = 0, // значение транфсофрмации .slider_wrapper
      _step = _itemWidth / _wrapperWidth * 100, // величина шага (для трансформации)
      _items = []; // массив элементов
    // наполнение массива _items
    _sliderItems.forEach(function (item, index) {
      _items.push({ item: item, position: index, transform: 0 });
    });

    var position = {
      getMin: 0,
      getMax: _items.length - 1
    };

    var _transformItem = function (direction) {
      if (direction === 'right') {
        if ((_positionLeftItem + _wrapperWidth / _itemWidth - 1) >= position.getMax) {
          return;
        }
        if (!_sliderControlLeft.classList.contains('slider__control_show5')) {
          _sliderControlLeft.classList.add('slider__control_show5');
        }
        if (_sliderControlRight.classList.contains('slider__control_show5') && (_positionLeftItem + _wrapperWidth / _itemWidth) >= position.getMax) {
          _sliderControlRight.classList.remove('slider__control_show5');
        }
        _positionLeftItem++;
        _transform -= _step;
      }
      if (direction === 'left') {
        if (_positionLeftItem <= position.getMin) {
          return;
        }
        if (!_sliderControlRight.classList.contains('slider__control_show5')) {
          _sliderControlRight.classList.add('slider__control_show5');
        }
        if (_sliderControlLeft.classList.contains('slider__control_show5') && _positionLeftItem - 1 <= position.getMin) {
          _sliderControlLeft.classList.remove('slider__control_show5');
        }
        _positionLeftItem--;
        _transform += _step;
      }
      _sliderWrapper.style.transform = 'translateX(' + _transform + '%)';
    };

    // обработчик события click для кнопок "назад" и "вперед"
    var _controlClick = function (e) {
      if (e.target.classList.contains('slider__control5')) {
        e.preventDefault();
        var direction = e.target.classList.contains('slider__control_right5') ? 'right' : 'left';
        _transformItem(direction);
      }
    };

    var _setUpListeners = function () {
      // добавление к кнопкам "назад" и "вперед" обрботчика _controlClick для событя click
      _sliderControls.forEach(function (item) {
        item.addEventListener('click', _controlClick);
      });
    };

    // инициализация
    _setUpListeners();

    return {
      right: function () { // метод right
        _transformItem('right');
      },
      left: function () { // метод left
        _transformItem('left');
      }
    }

  }
}());

let page = document.getElementById('body').getAttribute('data-value')

if(page == 'index'){
  var slider = multiItemSlider('.slider')
  var slider2 = multiItemSlider2('.slider2')
  var slider3 = multiItemSlider3('.slider3')
}
if(page == 'books'){
  var slider2 = multiItemSlider2('.slider2')
  var slider3 = multiItemSlider3('.slider3')
}
if(page == 'articles'){
  var slider = multiItemSlider('.slider')
  var slider4 = multiItemSlider4('.slider4')
}
if(page == 'personal_account'){
  var slider2 = multiItemSlider2('.slider2')
  var slider = multiItemSlider('.slider')
  var slider4 = multiItemSlider4('.slider4')
  var slider5 = multiItemSlider5('.slider5')
}
