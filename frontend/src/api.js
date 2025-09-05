import axios from 'axios';

const API_BASE = 'http://localhost:8000/api';

export const getRules = () => axios.get(`${API_BASE}/rules/`);
export const addRule = (data) => axios.post(`${API_BASE}/rules/`, data);
export const updateRule = (id, data) => axios.put(`${API_BASE}/rules/${id}/`, data);
export const deleteRule = (id) => axios.delete(`${API_BASE}/rules/${id}/`);

export const getDevices = () => axios.get(`${API_BASE}/devices/`);
export const addDevice = (data) => axios.post(`${API_BASE}/devices/`, data);
export const executeRuleOnDevice = (deviceId, ruleId) => 
    axios.post(`${API_BASE}/devices/${deviceId}/execute_rule/`, { rule_id: ruleId });

export const getDeviceOS = (deviceId) => axios.get(`${API_BASE}/os/?device=${deviceId}`);
export const getUsecases = () => axios.get(`${API_BASE}/usecases/`);
export const performUsecase = (deviceId, type) => 
    axios.post(`${API_BASE}/usecases/perform/`, { device_id: deviceId, type });