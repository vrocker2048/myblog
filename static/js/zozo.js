'use strict';

// back-to-top
$(document).ready((function (_this) {
  return function () {
    let bt
    bt = $('#back_to_top')
    if ($(document).width() > 480) {
      $(window).scroll(function () {
        let st
        st = $(window).scrollTop()
        if (st > 30) {
          return bt.css('display', 'block')
        } else {
          return bt.css('display', 'none')
        }
      })
      return bt.click(function () {
        $('body,html').animate({
          scrollTop: 0,
        }, 800)
        return false
      })
    }
  }
})(this))

// nav-toggle
$(document).ready((function (_this) {
  return function () {
    let nav,icon
    icon = $('#menu_icon')
    nav = $('#site_nav')
    icon.click(function () {
      nav.slideToggle(250)
    })
  }
})(this))

// 为超链接加上 target='_blank' 属性
$(document).ready(function() {
  $('p a[href^="http"]').each(function() {
    $(this).attr('target', '_blank');
  });
});

// // nav-toggle
// $(document).ready((function (_this) {
//   return function () {
//     let nav,icon
//     icon = $('#menu_icon')
//     nav = $('#site_nav')
//     if ($(document).width() < 768) {
//       nav.addClass('hide_block').removeClass('show_block')
//     }
//     return icon.click(function () {
//       if (!nav.hasClass('show_block')) {
//         return nav.addClass('show_block').removeClass('hide_block')
//       } else {
//         return nav.addClass('hide_block').removeClass('show_block')
//       }
//     })
//   }
// })(this))

// fancybox
// $(document).ready((function (_this) {
//   return function() {
//     if ($.fancybox) {
//       $('.zozo').each(function() {
//         $(this).find('img').each(function() {
//           $(this).wrap(`<div class="fancybox"><a href="${this.src}" data-fancybox="gallery" data-caption="${this.title}"></a></div>`);
//         });
//       });
//     }
//   };
// })(this))
