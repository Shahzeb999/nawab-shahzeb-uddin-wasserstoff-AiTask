<div class="wrap">
    <h1><?php echo esc_html(get_admin_page_title()); ?></h1>
    <form action="options.php" method="post">
        <?php
        settings_fields('rag_chatbot_options');
        do_settings_sections('rag_chatbot_options');
        ?>
        <table class="form-table">
            <tr valign="top">
                <th scope="row">API URL</th>
                <td><input type="text" name="rag_chatbot_api_url" value="<?php echo esc_attr(get_option('rag_chatbot_api_url')); ?>" /></td>
            </tr>
        </table>
        <?php submit_button(); ?>
    </form>
</div>