import request from '@/utils/myrequest'

export function getList(params) {
  return request({
    url: '/wechatUser/list',
    method: 'get',
    params
  })
}
