'use client';

import { useState, useEffect } from 'react';
import Link from 'next/link';
import { usePathname } from 'next/navigation';
import { useLanguage } from '@/context/LanguageContext';
import { useAuth } from '@/context/AuthContext';
import { siteConfig } from '@/lib/config';
import { Menu, X, Globe, User, LayoutDashboard } from 'lucide-react';
import { motion, AnimatePresence } from 'framer-motion';

const navLinks = [
  { name: 'home', href: '/' },
  { name: 'projects', href: '/projects' },
  { name: 'blog', href: '/blog' },
  { name: 'notes', href: '/notes' },
  { name: 'about', href: '/about' },
  { name: 'contact', href: '/contact' },
];

export default function Header() {
  const [isOpen, setIsOpen] = useState(false);
  const [scrolled, setScrolled] = useState(false);
  const { lang, t, toggleLang } = useLanguage();
  const { isAdmin } = useAuth();
  const pathname = usePathname();

  useEffect(() => {
    const handleScroll = () => setScrolled(window.scrollY > 20);
    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  return (
    <header 
      className={`sticky top-0 z-50 transition-all duration-300 ${
        scrolled ? 'bg-white/80 dark:bg-black/80 backdrop-blur-md shadow-sm' : 'bg-transparent'
      }`}
    >
      <nav className="container-custom h-20 flex items-center justify-between">
        <Link href="/" className="text-2xl font-bold flex items-center gap-2">
          <div className="w-8 h-8 bg-blue-600 rounded-lg flex items-center justify-center text-white text-xs">VH</div>
          <span>{siteConfig.name}</span>
        </Link>

        {/* Desktop Nav */}
        <div className="hidden md:flex items-center gap-8">
          {navLinks.map((link) => (
            <Link 
              key={link.name} 
              href={link.href}
              className={`relative py-1 group ${pathname === link.href ? 'text-blue-600 font-semibold' : ''}`}
            >
              {t.nav[link.name]}
              <motion.span 
                className="absolute bottom-0 left-0 w-0 h-0.5 bg-blue-600 transition-all group-hover:w-full"
                layoutId={pathname === link.href ? 'underline' : ''}
              />
            </Link>
          ))}
          <button 
            onClick={toggleLang}
            className="flex items-center gap-1 px-3 py-1 rounded-full border hover:bg-gray-100 dark:hover:bg-gray-800 transition-colors"
          >
            <Globe className="w-4 h-4" />
            <span className="uppercase text-sm font-medium">{lang}</span>
          </button>

          {isAdmin ? (
            <a 
              href="http://localhost:8000/admin/" 
              className="p-2 bg-blue-100 text-blue-600 rounded-lg hover:bg-blue-600 hover:text-white transition-all"
              title="Admin Panel"
            >
              <LayoutDashboard className="w-5 h-5" />
            </a>
          ) : (
            <a 
              href="http://localhost:8000/admin/login/" 
              className="p-2 hover:bg-gray-100 dark:hover:bg-gray-800 rounded-full transition-colors"
              title="Log In"
            >
              <User className="w-5 h-5" />
            </a>
          )}
        </div>

        {/* Mobile Toggle */}
        <button className="md:hidden" onClick={() => setIsOpen(true)}>
          <Menu className="w-6 h-6" />
        </button>
      </nav>

      {/* Mobile Menu */}
      <AnimatePresence>
        {isOpen && (
          <>
            <motion.div 
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              exit={{ opacity: 0 }}
              onClick={() => setIsOpen(false)}
              className="fixed inset-0 bg-black/50 backdrop-blur-sm z-50"
            />
            <motion.div 
              initial={{ x: '100%' }}
              animate={{ x: 0 }}
              exit={{ x: '100%' }}
              transition={{ type: 'spring', damping: 25, stiffness: 200 }}
              className="fixed right-0 top-0 bottom-0 w-4/5 max-w-sm bg-white dark:bg-gray-900 z-50 shadow-xl p-6 flex flex-col"
            >
              <div className="flex justify-between items-center mb-10">
                <span className="text-xl font-bold">{siteConfig.name}</span>
                <button onClick={() => setIsOpen(false)}>
                  <X className="w-6 h-6" />
                </button>
              </div>
              <div className="flex flex-col gap-6 text-lg">
                {navLinks.map((link) => (
                  <Link 
                    key={link.name} 
                    href={link.href} 
                    onClick={() => setIsOpen(false)}
                    className={pathname === link.href ? 'text-blue-600 font-semibold' : ''}
                  >
                    {t.nav[link.name]}
                  </Link>
                ))}
                <button 
                  onClick={() => { toggleLang(); setIsOpen(false); }}
                  className="flex items-center gap-2 px-4 py-2 border rounded-lg mt-4"
                >
                  <Globe className="w-5 h-5" />
                  <span className="uppercase font-medium">Switch to {lang === 'en' ? 'UKR' : 'EN'}</span>
                </button>

                <div className="pt-4 border-t">
                  {isAdmin ? (
                    <a 
                      href="http://localhost:8000/admin/" 
                      className="flex items-center gap-3 text-blue-600 font-bold"
                      onClick={() => setIsOpen(false)}
                    >
                      <LayoutDashboard className="w-6 h-6" />
                      <span>Admin Panel</span>
                    </a>
                  ) : (
                    <a 
                      href="http://localhost:8000/admin/login/" 
                      className="flex items-center gap-3 font-bold"
                      onClick={() => setIsOpen(false)}
                    >
                      <User className="w-6 h-6" />
                      <span>Log In</span>
                    </a>
                  )}
                </div>
              </div>
            </motion.div>
          </>
        )}
      </AnimatePresence>
    </header>
  );
}
