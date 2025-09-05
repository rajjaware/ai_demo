import React, { useEffect, useState } from 'react';
import { getDevices, getDeviceOS, getUsecases, performUsecase } from '../api';

function SWIMMPage() {
  const [devices, setDevices] = useState([]);
  const [selectedDevice, setSelectedDevice] = useState();
  const [os, setOS] = useState();
  const [usecases, setUsecases] = useState([]);

  useEffect(() => {
    getDevices().then(res => setDevices(res.data.filter(d => d.inventory_type === 'SWIMM')));
    getUsecases().then(res => setUsecases(res.data));
  }, []);

  const fetchOSInfo = async () => {
    const res = await getDeviceOS(selectedDevice);
    setOS(res.data.length ? res.data[0] : null);
  };

  const handlePerform = async (type) => {
    await performUsecase(selectedDevice, type);
    alert(`${type} usecase performed`);
  };

  return (
    <div>
      <h2>SWIMM - OS & Usecase Management</h2>
      <select onChange={e=>setSelectedDevice(e.target.value)}>
        <option value="">Select Device</option>
        {devices.map(dev => <option key={dev.id} value={dev.id}>{dev.name}</option>)}
      </select>
      <button onClick={fetchOSInfo}>Load OS Info</button>
      {os && <div>OS: {os.name} v{os.version}</div>}
      <div>
        <h3>Usecases</h3>
        <button onClick={()=>handlePerform('PRE')}>Perform PRE Usecase</button>
        <button onClick={()=>handlePerform('POST')}>Perform POST Usecase</button>
      </div>
    </div>
  );
}

export default SWIMMPage;