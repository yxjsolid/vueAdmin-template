<template>
  <div class="app-container">
    <el-table :data="list" v-loading.body="listLoading" element-loading-text="Loading" border fit highlight-current-row>


      <el-table-column align="center" label='ID' width="95">
        <template slot-scope="scope">
          {{scope.$index}}
        </template>
      </el-table-column>


      <el-table-column label="Name" width="200">
        <template slot-scope="scope">
          {{scope.row.name}}
        </template>
      </el-table-column>




      <el-table-column label="sex" width="110" align="center">
        <template slot-scope="scope">
          {{scope.row.sex}}
        </template>
      </el-table-column>


      <el-table-column label="头像" >
          <template slot-scope="scope">
            <img :src="scope.row.img" width="80" height="80"/>
          </template>
      </el-table-column>




    </el-table>
  </div>
</template>


<script>
import { getList } from '@/api/wechatUser'

export default {
  data() {
    return {
      list: null,
      listLoading: true
    }
  },
  filters: {
    statusFilter(status) {
      const statusMap = {
        published: 'success',
        draft: 'gray',
        deleted: 'danger'
      }
      return statusMap[status]
    }
  },
  created() {
    this.fetchData()
  },
  methods: {
    fetchData() {
      this.listLoading = true
      getList(this.listQuery).then(response => {
        this.list = response.data
        this.listLoading = false
      })
    }
  }
}
</script>
