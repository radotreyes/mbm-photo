$( '#image-{{ image.id }}' ).on( 'show.bs.modal', function() {
    $( '.modal .modal-body' ).css( 'overflow-y', 'auto' );
    $( '.modal .modal-body' ).css( 'max-height', $( window ).height() * 0.9 );
    $( 'img.in-modal' ).css( 'max-height', $( window ).height() * 0.85 );
    $( 'img.in-modal' ).css( 'width', 'auto' );
} );

$( '#image-{{ image.id }}' ).on( 'shown.bs.modal', function() {
  $( 'img.lazy' ).lazyload();
} );
