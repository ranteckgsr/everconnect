<?php
/*
Plugin Name: Custom EVF Entry API
Description: Exposes Everest Forms entries via custom REST API for published entries.
Version: 1.5
Author: Germanjit Randhawa
*/

add_action('rest_api_init', function () {
    register_rest_route('custom-evf/v1', '/entries', [
        'methods' => 'GET',
        'callback' => 'get_custom_evf_entries',
        'permission_callback' => function () {
            return current_user_can('edit_posts');
        },
    ]);
});

function get_custom_evf_entries(WP_REST_Request $request) {
    global $wpdb;

    $status = 'publish'; 

    $table_name = $wpdb->prefix . 'evf_entries';

    $query = $wpdb->prepare(
        "SELECT * FROM {$table_name} WHERE status = %s",
        $status
    );

    $entries = $wpdb->get_results($query, ARRAY_A);

    return rest_ensure_response($entries);
}
