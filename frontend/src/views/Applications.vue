<template>
  <div class="about">
    <h1 class="text-xl text-gray-500 ml-4 mt-12 border-l-4 border-gray-500 w-3/12"> &nbsp; &nbsp;My Applications</h1>



    <div class="relative overflow-x-auto px-16 mt-12 rounded">
      <table class="w-full text-sm text-left rtl:text-right text-gray-500">
        <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400 border-b">
          <tr>
            <th scope="col" class="px-6 py-3">
              Title
            </th>
            <th scope="col" class="">
              Company
            </th>
            <th scope="col" class="">
              Location
            </th>
            <th scope="col" class="">
              Status
            </th>
            <th scope="col" class="">
              Submitted
            </th>
            <th scope="col" class="">
              Deadline
            </th>
            <th scope="col" class="">
              Action
            </th>
          </tr>
        </thead>
        <tbody>
          <tr class="bg-white border-b">
            <th scope="row" class="px-6 py-2 font-medium text-gray-900 whitespace-nowrap">
              Apple MacBook Pro 17"
            </th>
            <td class="">
              Silver
            </td>
            <td class="">
              Laptop
            </td>
            <td class="">
              $2999
            </td>
            <td class="">
              $2999
            </td>
            <td class="">
              $2999
            </td>
            <td class="">
             Withdraw
            </td>
          </tr>
          
        </tbody>
      </table>
    </div>


  </div>
</template>
<script>

export default {
  name: 'applications',
  mounted() {
    
    document.title = 'Applications | Djobs';
  },
  

}
</script>