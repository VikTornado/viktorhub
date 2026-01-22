'use client';

import React, { useState } from 'react';
import { motion } from 'framer-motion';
import { useLanguage } from '@/context/LanguageContext';
import { sendContact } from '@/lib/api';
import { Send, CheckCircle, AlertCircle } from 'lucide-react';

export default function ContactPage() {
  const { t } = useLanguage();
  const [formData, setFormData] = useState({ name: '', email: '', subject: '', message: '' });
  const [status, setStatus] = useState('idle'); // idle, loading, success, error

  const handleSubmit = async (e) => {
    e.preventDefault();
    setStatus('loading');
    try {
      await sendContact(formData);
      setStatus('success');
      setFormData({ name: '', email: '', subject: '', message: '' });
    } catch (err) {
      console.error(err);
      setStatus('error');
    }
  };

  return (
    <div className="container-custom py-20 max-w-2xl">
      <motion.div 
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
      >
        <h1 className="text-4xl font-bold mb-4">{t.contact.title}</h1>
        <p className="text-gray-600 dark:text-gray-400 mb-12">
          Have a project in mind or just want to say hi? Feel free to reach out using the form below!
        </p>

        <form onSubmit={handleSubmit} className="space-y-6">
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div className="flex flex-col gap-2">
              <label className="text-sm font-semibold">{t.contact.name}</label>
              <input 
                required
                type="text" 
                value={formData.name}
                onChange={(e) => setFormData({...formData, name: e.target.value})}
                className="p-3 border rounded-xl outline-none focus:ring-2 focus:ring-blue-600 dark:bg-gray-800 transition-all transition-colors"
                placeholder="John Doe"
              />
            </div>
            <div className="flex flex-col gap-2">
              <label className="text-sm font-semibold">{t.contact.email}</label>
              <input 
                required
                type="email" 
                value={formData.email}
                onChange={(e) => setFormData({...formData, email: e.target.value})}
                className="p-3 border rounded-xl outline-none focus:ring-2 focus:ring-blue-600 dark:bg-gray-800 transition-all transition-colors"
                placeholder="john@example.com"
              />
            </div>
          </div>
          <div className="flex flex-col gap-2">
            <label className="text-sm font-semibold">{t.contact.subject}</label>
            <input 
              required
              type="text" 
              value={formData.subject}
              onChange={(e) => setFormData({...formData, subject: e.target.value})}
              className="p-3 border rounded-xl outline-none focus:ring-2 focus:ring-blue-600 dark:bg-gray-800 transition-all transition-colors"
              placeholder="Project Inquiry"
            />
          </div>
          <div className="flex flex-col gap-2">
            <label className="text-sm font-semibold">{t.contact.message}</label>
            <textarea 
              required
              rows={5}
              value={formData.message}
              onChange={(e) => setFormData({...formData, message: e.target.value})}
              className="p-3 border rounded-xl outline-none focus:ring-2 focus:ring-blue-600 dark:bg-gray-800 transition-all transition-colors resize-none"
              placeholder="Tell me more..."
            />
          </div>

          <button 
            type="submit" 
            disabled={status === 'loading'}
            className="w-full py-4 bg-blue-600 text-white rounded-xl font-bold flex items-center justify-center gap-2 hover:bg-blue-700 disabled:opacity-50 transition-all"
          >
            {status === 'loading' ? 'Sending...' : (
              <>
                {t.contact.send}
                <Send className="w-5 h-5" />
              </>
            )}
          </button>

          {status === 'success' && (
            <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} className="flex items-center gap-2 text-green-600 font-medium">
              <CheckCircle className="w-5 h-5" /> {t.contact.success}
            </motion.div>
          )}
          {status === 'error' && (
            <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} className="flex items-center gap-2 text-red-600 font-medium">
              <AlertCircle className="w-5 h-5" /> {t.contact.error}
            </motion.div>
          )}
        </form>
      </motion.div>
    </div>
  );
}
