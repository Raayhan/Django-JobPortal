<template>
    <div class="border border-indigo-200 bg-indigo-50 p-4 mx-4 rounded">
        <div class="text-indigo-700 font-bold text-sm">{{ job.title }}</div>
        <div class="text-sm text-gray-600">Salary : {{ job.salary }} ৳</div>
        <div class=" rounded-lg text-xs text-orange-700">#{{ job.category_name }}</div>
    </div>

</template>
<script>
export default {
    name: 'JobBox',
    props: {
        job: Object
    }

}
</script>