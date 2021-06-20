async function up () {
  await new Promise((resolve, reject) => {
    setTimeout(()=> { resolve('upped'); }, 3000);
  });
}

/**
 * Make any changes that UNDO the up function side effects here (if possible)
 */
async function down () {
  await new Promise((resolve, reject) => {
    setTimeout(()=> { resolve('downed'); }, 3000);
  });
}

module.exports = { up, down };