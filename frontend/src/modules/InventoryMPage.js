import React, { useEffect, useState } from 'react';
import { getDevices, addDevice, executeRuleOnDevice, getRules } from '../api';

function InventoryMPage() {
  const [devices, setDevices] = useState([]);
  const [form, setForm] = useState({name:'',inventory_type:'InventoryM'});
  const [rules, setRules] = useState([]);
  const [selectedDevice, setSelectedDevice] = useState();
  const [selectedRule, setSelectedRule] = useState();

  useEffect(() => {
    getDevices().then(res => setDevices(res.data));
    getRules().then(res => setRules(res.data));
  }, []);

  const handleAdd = async () => {
    await addDevice(form);
    getDevices().then(res => setDevices(res.data));
    setForm({name:'',inventory_type:'InventoryM'});
  };

  const handleExecute = async () => {
    await executeRuleOnDevice(selectedDevice, selectedRule);
    alert('Rule executed!');
  };

  return (
    <div>
      <h2>InventoryM - Device Management</h2>
      <input placeholder="Device Name" value={form.name} onChange={e=>setForm({...form,name:e.target.value})}/>
      <button onClick={handleAdd}>Add Device</button>
      <ul>
        {devices.map(device => (
          <li key={device.id}>{device.name}</li>
        ))}
      </ul>
      <h3>Execute Rule on Device</h3>
      <select onChange={e=>setSelectedDevice(e.target.value)}>
        <option value="">Select Device</option>
        {devices.map(dev => <option key={dev.id} value={dev.id}>{dev.name}</option>)}
      </select>
      <select onChange={e=>setSelectedRule(e.target.value)}>
        <option value="">Select Rule</option>
        {rules.map(rule => <option key={rule.id} value={rule.id}>{rule.name}</option>)}
      </select>
      <button onClick={handleExecute}>Execute Rule</button>
    </div>
  );
}

export default InventoryMPage;