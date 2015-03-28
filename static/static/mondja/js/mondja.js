$(function () {

    // オプションのproximityでbottom.jsを発生する位置を指定する
    $(window).bottom({ proximity: 0.05 });
    $(window).bind('bottom', function () {

        var obj = $(this);

        // 「loading」がfalseの時に実行
        if (!obj.data('loading')) {

            // 「loading」をtrueにする
            obj.data('loading', true);

            // ローディング画像を表示
            $('#loadimg').html('<p><i class="fa fa-spinner fa-pulse fa-2x"></i></p>');

            // 追加したい処理を記述
            setTimeout(function () {

                // ローディング画像を削除
                $('#loadimg').html('');

                // 追加するHTMLを指定
                $('#wrap').append('<div class="box">test</div><div class="box">test</div><div class="box">test</div>');

                // 処理が完了したら「loading」をfalseにする
                obj.data('loading', false);

            }, 1500);
        }

    });

    // リロードしたときにページの先頭を表示する
    $('html,body').animate({ scrollTop: 0 }, '1');

});
