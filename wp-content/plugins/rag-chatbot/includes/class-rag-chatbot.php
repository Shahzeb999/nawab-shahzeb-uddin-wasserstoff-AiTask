<?php

class RAG_Chatbot {

    protected $loader;
    protected $plugin_name;
    protected $version;

    public function __construct() {
        $this->plugin_name = 'rag-chatbot';
        $this->version = RAG_CHATBOT_VERSION;
        $this->load_dependencies();
        $this->set_locale();
        $this->define_admin_hooks();
        $this->define_public_hooks();
    }

    private function load_dependencies() {
        require_once plugin_dir_path(dirname(__FILE__)) . 'includes/class-settings.php';
        require_once plugin_dir_path(dirname(__FILE__)) . 'includes/functions.php';
    }

    private function set_locale() {
        add_action('plugins_loaded', array($this, 'load_plugin_textdomain'));
    }

    private function define_admin_hooks() {
        $settings = new RAG_Chatbot_Settings($this->get_plugin_name(), $this->get_version());
        add_action('admin_menu', array($settings, 'add_settings_page'));
        add_action('admin_init', array($settings, 'register_settings'));
    }

    private function define_public_hooks() {
        add_action('wp_enqueue_scripts', array($this, 'enqueue_styles'));
        add_action('wp_enqueue_scripts', array($this, 'enqueue_scripts'));
        add_shortcode('rag_chatbot', array($this, 'chatbot_shortcode'));
    }

    public function load_plugin_textdomain() {
        load_plugin_textdomain(
            'rag-chatbot',
            false,
            dirname(dirname(plugin_basename(__FILE__))) . '/languages/'
        );
    }

    public function enqueue_styles() {
        wp_enqueue_style($this->plugin_name, plugin_dir_url(dirname(__FILE__)) . 'public/css/public.css', array(), $this->version, 'all');
    }

    public function enqueue_scripts() {
        wp_enqueue_script($this->plugin_name, plugin_dir_url(dirname(__FILE__)) . 'public/js/chatbot.js', array('jquery'), $this->version, false);
    }

    public function chatbot_shortcode($atts) {
        ob_start();
        include plugin_dir_path(dirname(__FILE__)) . 'public/partials/chatbot-widget.php';
        return ob_get_clean();
    }

    public function run() {
        $this->load_dependencies();
        $this->set_locale();
        $this->define_admin_hooks();
        $this->define_public_hooks();
    }

    public function get_plugin_name() {
        return $this->plugin_name;
    }

    public function get_version() {
        return $this->version;
    }
}