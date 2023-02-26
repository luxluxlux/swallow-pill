// TODO Move to appropriate folder
import { createSlice } from '@reduxjs/toolkit'

export const pageSlice = createSlice({
  name: 'page',
  initialState: {
    value: 'schedule'
  },
  reducers: {
    setPage: (state, action) => {
      state.value = action.payload
    }
  }
})

export const { setPage } = pageSlice.actions

export default pageSlice.reducer