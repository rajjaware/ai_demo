import React, { useEffect, useState } from 'react';
import { getRules, addRule, updateRule, deleteRule } from '../api';

function ICMMPage() {
  const [rules, setRules] = useState([]);
  const [form, setForm] = useState({name:'',description:''});

  useEffect(() => { getRules().then(res => setRules(res.data)); }, []);
  
  const handleAdd = async () => {
    await addRule(form);
    getRules().then(res => setRules(res.data));
    setForm({name:'',description:''});
  };

  return (
    <div>
      <h2>ICMM - Rules Management</h2>
      <input placeholder="Rule Name" value={form.name} onChange={e=>setForm({...form,name:e.target.value})}/>
      <input placeholder="Description" value={form.description} onChange={e=>setForm({...form,description:e.target.value})}/>
      <button onClick={handleAdd}>Add Rule</button>
      <ul>
        {rules.map(rule => (
          <li key={rule.id}>{rule.name}: {rule.description}</li>
        ))}
      </ul>
    </div>
  );
}

export default ICMMPage;