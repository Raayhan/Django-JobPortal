<script>
export default {
    name: 'BaseModal',
    props: {
        show: {
            type: Boolean,
        }
    }
};
</script>

<template>
    <!-- Render inside our `<div id="modals"></div>` in index.html -->
    <Teleport to="#modals">
        <!-- Show / hide the modal -->
        <div v-if="show" class="">
            <!-- The backdrop -->
            <div class="fixed inset-0 bg-gray-900 opacity-40 duration-300"></div>

            <!-- Where the actual content goes -->
            <div class="fixed inset-0 flex items-center justify-center">
                <div class="bg-white text-gray-600 rounded">
                    <slot></slot>
                </div>
            </div>
        </div>
    </Teleport>
</template>